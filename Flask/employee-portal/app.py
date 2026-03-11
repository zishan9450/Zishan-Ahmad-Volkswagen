from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.secret_key = "secret123"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flaskuser:root@localhost/fsd"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ─── Models ───────────────────────────────────────────────────────────────────

class User(db.Model):
    __tablename__ = "users"
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role     = db.Column(db.String(20))   # admin / manager / employee

class Employee(db.Model):
    __tablename__ = "employees"
    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(100))
    email      = db.Column(db.String(100), unique=True)
    department = db.Column(db.String(100))
    manager_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=True)
    user_id    = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True)

with app.app_context():
    db.create_all()

# ─── Seed Data ────────────────────────────────────────────────────────────────

@app.route("/seed")
def seed():
    if User.query.first():
        return "Already seeded!"

    # Create users
    u1 = User(username="alice",   password="admin123",   role="admin")
    u2 = User(username="bob",     password="manager123", role="manager")
    u3 = User(username="charlie", password="emp123",     role="employee")
    u4 = User(username="diana",   password="emp123",     role="employee")
    u5 = User(username="eve",     password="emp123",     role="employee")
    db.session.add_all([u1, u2, u3, u4, u5])
    db.session.commit()

    # Create employees linked to users
    e1 = Employee(name="Alice",   email="alice@test.com",   department="IT",  manager_id=None, user_id=u1.id)
    e2 = Employee(name="Bob",     email="bob@test.com",     department="IT",  manager_id=None, user_id=u2.id)
    db.session.add_all([e1, e2])
    db.session.commit()

    e3 = Employee(name="Charlie", email="charlie@test.com", department="IT",  manager_id=e2.id, user_id=u3.id)
    e4 = Employee(name="Diana",   email="diana@test.com",   department="IT",  manager_id=e2.id, user_id=u4.id)
    e5 = Employee(name="Eve",     email="eve@test.com",     department="HR",  manager_id=None,  user_id=u5.id)
    db.session.add_all([e3, e4, e5])
    db.session.commit()

    return redirect("/login")

# ─── Decorators ───────────────────────────────────────────────────────────────

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated

def role_required(*roles):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if session.get("role") not in roles:
                return render_template("error.html", message="Access Denied: Insufficient permissions.")
            return f(*args, **kwargs)
        return decorated
    return wrapper

# ─── Auth Routes ──────────────────────────────────────────────────────────────

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            employee = Employee.query.filter_by(user_id=user.id).first()
            session["user_id"]    = user.id
            session["role"]       = user.role
            session["username"]   = user.username
            session["emp_id"]     = employee.id if employee else None
            return redirect("/employees" if user.role in ["admin", "manager"] else f"/employee/{employee.id}")
        error = "Invalid username or password."
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ─── Employee Routes ──────────────────────────────────────────────────────────

# View all employees — Admin & Manager only
@app.route("/employees")
@login_required
@role_required("admin", "manager")
def employees():
    all_employees = Employee.query.all()
    return render_template("employees.html", employees=all_employees)

# View a single profile
@app.route("/employee/<int:id>")
@login_required
def profile(id):
    role   = session["role"]
    emp_id = session["emp_id"]
    if role == "employee" and emp_id != id:
        return render_template("error.html", message="Access Denied: You can only view your own profile.")
    employee = Employee.query.get_or_404(id)
    user     = User.query.get(employee.user_id)
    # Fetch manager's employee record using manager_id
    manager  = Employee.query.get(employee.manager_id) if employee.manager_id else None
    return render_template("profile.html", employee=employee, user=user, manager=manager)


# Edit employee
@app.route("/employee/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit(id):
    role     = session["role"]
    emp_id   = session["emp_id"]
    user_id  = session["user_id"]
    employee = Employee.query.get_or_404(id)

    # Access control
    if role == "employee" and emp_id != id:
        return render_template("error.html", message="Access Denied: You can only edit your own profile.")
    if role == "manager":
        # Manager can only edit employees whose manager_id = manager's employee id
        manager_emp = Employee.query.filter_by(user_id=user_id).first()
        if employee.manager_id != manager_emp.id:
            return render_template("error.html", message="Access Denied: You can only edit your team members.")

    if request.method == "POST":
        employee.name       = request.form["name"]
        employee.email      = request.form["email"]
        employee.department = request.form["department"]
        # Only admin can assign roles and managers
        if role == "admin":
            user = User.query.get(employee.user_id)
            user.role          = request.form["role"]
            employee.manager_id = request.form.get("manager_id") or None
        db.session.commit()
        return redirect(f"/employee/{id}")

    managers = Employee.query.join(User, Employee.user_id == User.id).filter(User.role == "manager").all()
    user     = User.query.get(employee.user_id)
    return render_template("edit.html", employee=employee, user=user, managers=managers, role=role)

# Delete employee — Admin only
@app.route("/employee/<int:id>/delete")
@login_required
@role_required("admin")
def delete(id):
    employee = Employee.query.get_or_404(id)
    # Also delete the linked user
    user = User.query.get(employee.user_id)
    db.session.delete(employee)
    if user:
        db.session.delete(user)
    db.session.commit()
    return redirect("/employees")

if __name__ == "__main__":
    app.run(debug=True)
