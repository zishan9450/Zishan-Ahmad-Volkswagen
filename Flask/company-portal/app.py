from flask import Flask
from blueprints.auth.routes     import auth_bp
from blueprints.admin.routes    import admin_bp
from blueprints.employee.routes import employee_bp
from blueprints.hr.routes       import hr_bp

app = Flask(__name__)
app.secret_key = "company_portal_secret"

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(hr_bp)

if __name__ == "__main__":
    app.run(debug=True, port=4000)
