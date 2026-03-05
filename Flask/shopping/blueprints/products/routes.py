import json
from flask import Blueprint, render_template, request, make_response, redirect, url_for

products_bp = Blueprint("products", __name__, url_prefix="/products")

PRODUCTS = [
    {"id": "laptop",     "name": "Laptop",      "price": 75000},
    {"id": "mouse",      "name": "Mouse",        "price": 999},
    {"id": "keyboard",   "name": "Keyboard",     "price": 1499},
    {"id": "monitor",    "name": "Monitor",      "price": 18000},
    {"id": "headphones", "name": "Headphones",   "price": 2999},
]

@products_bp.route("/")
def index():
    return render_template("products/index.html", products=PRODUCTS)

@products_bp.route("/add/<product_id>", methods=["POST"])
def add_to_cart(product_id):
    # Read existing cart from cookie
    cart_cookie = request.cookies.get("cart")
    cart = json.loads(cart_cookie) if cart_cookie else {}

    # Increment quantity
    cart[product_id] = cart.get(product_id, 0) + 1

    response = make_response(redirect(url_for("products.index")))
    response.set_cookie("cart", json.dumps(cart))
    return response
