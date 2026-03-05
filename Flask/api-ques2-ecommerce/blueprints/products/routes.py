import json
from flask import Blueprint, request, jsonify, session, make_response

products_bp = Blueprint("products", __name__, url_prefix="/products")

PRODUCTS = [
    {"id": 1, "name": "Laptop",     "price": 70000},
    {"id": 2, "name": "Mouse",      "price": 500},
    {"id": 3, "name": "Keyboard",   "price": 1200},
    {"id": 4, "name": "Monitor",    "price": 18000},
    {"id": 5, "name": "Headphones", "price": 2999},
]

MAX_RECENT = 5

def find_product(product_id):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    return None


# API 2: Get all products
@products_bp.route("/", methods=["GET"])
def get_all_products():
    return jsonify(PRODUCTS), 200


# API 3: View a product — stores in recently viewed cookie
@products_bp.route("/<int:product_id>", methods=["GET"])
def view_product(product_id):
    # Check if user is logged in
    if "username" not in session:
        return jsonify({"error": "Unauthorized. Please login first."}), 401

    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Read existing recently viewed from cookie
    recent_cookie = request.cookies.get("recent_products")
    recent = json.loads(recent_cookie) if recent_cookie else []

    # Remove if already exists (to re-add at front)
    if product_id in recent:
        recent.remove(product_id)

    # Add to front of list
    recent.insert(0, product_id)

    # Keep only last MAX_RECENT (5) products
    recent = recent[:MAX_RECENT]

    response = make_response(jsonify({
        "product":        product,
        "recently_viewed": recent
    }), 200)

    # Save updated list back to cookie
    response.set_cookie("recent_products", json.dumps(recent))
    return response


# API 4: Get recently viewed products
@products_bp.route("/recently-viewed", methods=["GET"])
def recently_viewed():
    # Check if user is logged in
    if "username" not in session:
        return jsonify({"error": "Unauthorized. Please login first."}), 401

    recent_cookie = request.cookies.get("recent_products")

    if not recent_cookie:
        return jsonify({"message": "No recently viewed products", "products": []}), 200

    recent_ids = json.loads(recent_cookie)

    # Return product details in order of recently viewed
    recent_products = []
    for pid in recent_ids:
        product = find_product(pid)
        if product:
            recent_products.append({"id": product["id"], "name": product["name"]})

    return jsonify(recent_products), 200
