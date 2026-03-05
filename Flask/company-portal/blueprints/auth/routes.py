import json
from flask import Blueprint, request, render_template, make_response, redirect, url_for

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username    = request.form.get("username", "").strip()
        password    = request.form.get("password", "").strip()
        role        = request.form.get("role", "").strip()
        remember_me = request.form.get("remember_me")

        # Validate fields
        if not username or not password or not role:
            error = "All fields are required."
        else:
            max_age = 7 * 24 * 60 * 60 if remember_me else None

            role_redirects = {
                "admin":    url_for("admin.dashboard"),
                "employee": url_for("employee.dashboard"),
                "hr":       url_for("hr.dashboard"),
            }

            response = make_response(redirect(role_redirects[role]))
            response.set_cookie("username",  username, max_age=max_age)
            response.set_cookie("user_role", role,     max_age=max_age)
            return response

    return render_template("auth/login.html", error=error)


@auth_bp.route("/logout")
def logout():
    response = make_response(redirect(url_for("auth.login")))
    response.delete_cookie("username")
    response.delete_cookie("user_role")
    return response
