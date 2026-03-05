from flask import Blueprint, request, render_template, redirect, url_for

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/dashboard")
def dashboard():
    username  = request.cookies.get("username")
    user_role = request.cookies.get("user_role")

    if not username or user_role != "admin":
        return redirect(url_for("auth.login"))

    return render_template("admin/dashboard.html", username=username)
