from flask import Flask
from blueprints.auth.routes     import auth_bp
from blueprints.products.routes import products_bp

app = Flask(__name__)
app.secret_key = "ecommerce_secret"

app.register_blueprint(auth_bp)
app.register_blueprint(products_bp)

if __name__ == "__main__":
    app.run(debug=True)
