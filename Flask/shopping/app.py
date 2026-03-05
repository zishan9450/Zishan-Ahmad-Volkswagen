from flask import Flask
from blueprints.products.routes import products_bp
from blueprints.cart.routes     import cart_bp
from blueprints.orders.routes   import orders_bp

app = Flask(__name__)
app.secret_key = "shopping_secret"

app.register_blueprint(products_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(orders_bp)

if __name__ == "__main__":
    app.run(debug=True, port=4000)
