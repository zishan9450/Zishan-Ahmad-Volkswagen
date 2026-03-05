from flask import Blueprint, request, jsonify, session

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Fake users
USERS = {
    "zishan": "pass123",
    "john":   "pass456",
}

# API 1: Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data     = request.get_json()
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if username not in USERS or USERS[username] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    # Store username in session
    session["username"] = username
    return jsonify({"message": f"Welcome {username}!", "username": username}), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logged out successfully"}), 200
