from flask import Blueprint, request, render_template, redirect, url_for

hr_bp = Blueprint("hr", __name__, url_prefix="/hr")

@hr_bp.route("/dashboard")
def dashboard():
    username  = request.cookies.get("username")
    user_role = request.cookies.get("user_role")

    if not username or user_role != "hr":
        return redirect(url_for("auth.login"))

    return render_template("hr/dashboard.html", username=username)
