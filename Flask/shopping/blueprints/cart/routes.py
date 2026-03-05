import json
from flask import Blueprint, render_template, request, make_response, redirect, url_for

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")

PRODUCTS = {
    "laptop":     {"name": "Laptop",     "price": 75000},
    "mouse":      {"name": "Mouse",      "price": 999},
    "keyboard":   {"name": "Keyboard",   "price": 1499},
    "monitor":    {"name": "Monitor",    "price": 18000},
    "headphones": {"name": "Headphones", "price": 2999},
}

@cart_bp.route("/")
def index():
    cart_cookie = request.cookies.get("cart")

    if not cart_cookie:
        return render_template("cart/index.html", cart_items=[], total=0, empty=True)

    cart = json.loads(cart_cookie)

    cart_items = []
    total = 0
    for product_id, qty in cart.items():
        product = PRODUCTS.get(product_id)
        if product:
            subtotal = product["price"] * qty
            total   += subtotal
            cart_items.append({
                "id":       product_id,
                "name":     product["name"],
                "price":    product["price"],
                "qty":      qty,
                "subtotal": subtotal,
            })

    return render_template("cart/index.html", cart_items=cart_items, total=total, empty=False)


@cart_bp.route("/update/<product_id>/<action>", methods=["POST"])
def update(product_id, action):
    cart_cookie = request.cookies.get("cart")
    cart = json.loads(cart_cookie) if cart_cookie else {}

    if product_id in cart:
        if action == "increase":
            cart[product_id] += 1
        elif action == "decrease":
            cart[product_id] -= 1
            if cart[product_id] <= 0:
                del cart[product_id]   # remove if qty hits 0

    response = make_response(redirect(url_for("cart.index")))
    response.set_cookie("cart", json.dumps(cart))
    return response


@cart_bp.route("/clear")
def clear():
    response = make_response(redirect(url_for("cart.index")))
    response.delete_cookie("cart")
    return response
