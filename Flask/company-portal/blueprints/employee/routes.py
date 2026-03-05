from flask import Blueprint, request, render_template, redirect, url_for

employee_bp = Blueprint("employee", __name__, url_prefix="/employee")

@employee_bp.route("/dashboard")
def dashboard():
    username  = request.cookies.get("username")
    user_role = request.cookies.get("user_role")

    if not username or user_role != "employee":
        return redirect(url_for("auth.login"))

    return render_template("employee/dashboard.html", username=username)
