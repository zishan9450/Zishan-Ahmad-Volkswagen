from flask import Flask, request, render_template, make_response, redirect, url_for


app = Flask(__name__)

# # ─── Question 1 Data ───────────────────────────────────────
# products = [
#     {"id": 1, "name": "Laptop",     "category": "Electronics", "price": 1200, "available": True},
#     {"id": 2, "name": "T-Shirt",    "category": "Clothing",    "price": 25,   "available": True},
#     {"id": 3, "name": "Headphones", "category": "Electronics", "price": 150,  "available": False},
#     {"id": 4, "name": "Jeans",      "category": "Clothing",    "price": 60,   "available": True},
# ]

# # ─── Question 2 Data ───────────────────────────────────────
# employees = [
#     {"id": 1, "name": "Zishan Ahmad", "department": "Engineering", "salary": 95000},
#     {"id": 2, "name": "Priya Sharma", "department": "Design",      "salary": 72000},
#     {"id": 3, "name": "Rahul Verma",  "department": "Marketing",   "salary": 65000},
#     {"id": 4, "name": "Neha Gupta",   "department": "HR",          "salary": 58000},
# ]

# roles_config = {
#     "admin": {
#         "title": "Admin Dashboard",
#         "can_see_salary": True,
#         "can_delete": True,
#         "nav_links": ["Users", "Reports", "Settings", "Audit Logs"],
#     },
#     "manager": {
#         "title": "Manager Dashboard",
#         "can_see_salary": True,
#         "can_delete": False,
#         "nav_links": ["Team", "Reports", "Attendance"],
#     },
#     "employee": {
#         "title": "Employee Dashboard",
#         "can_see_salary": False,
#         "can_delete": False,
#         "nav_links": ["My Profile", "Attendance", "Leave Requests"],
#     },
# }

# # ─── Question 3 Data ───────────────────────────────────────
# comments = [
#     {"username": "john",  "comment": "  This product is good  ",                        "likes": 120, "flagged": False},
#     {"username": "sarah", "comment": "  Totally dumb decision by the company!  ",        "likes": 45,  "flagged": True},
#     {"username": "mike",  "comment": "  Absolutely love it, best purchase ever!  ",      "likes": 210, "flagged": False},
#     {"username": "emma",  "comment": "  That was stupid of them to do.  ",               "likes": 30,  "flagged": True},
#     {"username": "alex",  "comment": "  " + "This is a very long comment. " * 8 + "  ", "likes": 88,  "flagged": False},
#     {"username": "priya", "comment": "  Great quality and fast delivery!  ",             "likes": 175, "flagged": False},
# ]

# BANNED_WORDS = ["dumb", "stupid", "idiot", "fool"]

# def clean_comment(comment):
#     for word in BANNED_WORDS:
#         comment = comment.replace(word, "***")
#     return comment.strip()


# # ─── Question 1 Routes ─────────────────────────────────────
# @app.route("/")
# def home():
#     return render_template("index.html", products=products, total=len(products))

# @app.route("/products")
# def get_products():
#     category  = request.args.get("category")
#     available = request.args.get("available")
#     sort      = request.args.get("sort")

#     result = products.copy()

#     if category:
#         result = [p for p in result if p["category"].lower() == category.lower()]

#     if available:
#         is_available = available.lower() == "true"
#         result = [p for p in result if p["available"] == is_available]

#     if sort == "low-to-high":
#         result = sorted(result, key=lambda p: p["price"])
#     elif sort == "high-to-low":
#         result = sorted(result, key=lambda p: p["price"], reverse=True)

#     return render_template("index.html", products=result, total=len(result))


# # ─── Question 2 Route ──────────────────────────────────────
# @app.route("/dashboard")
# def dashboard():
#     role   = request.args.get("role", "employee").lower()
#     config = roles_config.get(role, roles_config["employee"])
#     return render_template("dashboard.html", role=role, config=config, employees=employees)


# # ─── Question 3 Route ──────────────────────────────────────
# @app.route("/comments")
# def show_comments():
#     processed = []
#     for c in comments:
#         processed.append({
#             "username": c["username"].upper(),
#             "comment":  clean_comment(c["comment"]),
#             "likes":    c["likes"],
#             "flagged":  c["flagged"],
#         })

#     total_comments = len(processed)
#     total_flagged  = sum(1 for c in processed if c["flagged"])
#     most_liked     = max(processed, key=lambda c: c["likes"])
#     all_usernames  = ", ".join(c["username"] for c in processed)

#     return render_template(
#         "comments.html",
#         comments       = processed,
#         total_comments = total_comments,
#         total_flagged  = total_flagged,
#         most_liked     = most_liked,
#         all_usernames  = all_usernames,
#     )

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     errors = {}
#     form_data = {"email": "", "password": ""}

#     if request.method == "POST":
#         email    = request.form.get("email", "").strip()
#         password = request.form.get("password", "").strip()

#         form_data = {"email": email, "password": password}

#         # 1. Blank check
#         if not email:
#             errors["email"] = "Email should not be blank."
#         elif "@" not in email:
#             # 2. Email must have @ symbol
#             errors["email"] = "Invalid email. Must contain @ symbol."

#         if not password:
#             errors["password"] = "Password should not be blank."
#         elif len(password) < 5 or len(password) > 8:
#             # 3. Password length 5–8
#             errors["password"] = "Password must be atleast 5 and maximum 8 characters."

#         if not errors:
#             return render_template("login.html", success=True, form_data=form_data, errors={})

#     return render_template("login.html", success=False, form_data=form_data, errors=errors)






@app.route("/cookie", methods=["GET", "POST"])
def cookie_form():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if username:
            response = make_response(redirect(url_for("setname")))
            response.set_cookie("username", username)
            response.set_cookie("visit_count", "0")
            return response
    return render_template("cookie_form.html")


@app.route("/setname")
def setname():
    username = request.cookies.get("username")
    if not username:
        return redirect(url_for("cookie_form"))
    return render_template("setname.html", username=username)


@app.route("/visit")
def visit():
    username    = request.cookies.get("username")
    visit_count = request.cookies.get("visit_count", "0")

    if not username:
        return redirect(url_for("cookie_form"))

    visit_count = int(visit_count) + 1

    response = make_response(render_template(
        "visit.html",
        username    = username,
        visit_count = visit_count
    ))
    response.set_cookie("visit_count", str(visit_count))
    return response


@app.route("/clear")
def clear():
    response = make_response(redirect(url_for("cookie_form")))
    response.delete_cookie("username")
    response.delete_cookie("visit_count")
    return response



if __name__ == "__main__":
    app.run(debug=True, port=3000)

