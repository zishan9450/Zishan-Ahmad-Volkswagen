# from flask import Flask, jsonify, request

# app = Flask(__name__)

# products = [
#     {"id": 1, "name": "Laptop", "price": 50000},
#     {"id": 2, "name": "Phone",  "price": 20000}
# ]

# @app.route("/api/products", methods=["GET"])
# def get_products():
#     return jsonify(products), 200

# @app.route("/api/products/<int:product_id>", methods=["GET"])
# def get_product(product_id):
#     for p in products:
#         if p["id"] == product_id:
#             return jsonify(p), 200
#     return jsonify({"error": "Product not found"}), 404

# @app.route("/api/products", methods=["POST"])
# def create_product():
#     data = request.get_json()
#     if "name" not in data or "price" not in data:
#         return jsonify({"error": "Invalid input"}), 400
#     new_product = {
#         "id":    len(products) + 1,
#         "name":  data["name"],
#         "price": data["price"]
#     }
#     products.append(new_product)
#     return jsonify(new_product), 201

# @app.route("/api/products/<int:product_id>", methods=["PUT"])
# def update_product(product_id):
#     data = request.get_json()
#     for p in products:
#         if p["id"] == product_id:
#             if "name"  in data: p["name"]  = data["name"]
#             if "price" in data: p["price"] = data["price"]
#             return jsonify(p), 200
#     return jsonify({"error": "Product not found"}), 404

# @app.route("/api/products/<int:product_id>", methods=["DELETE"])
# def delete_product(product_id):
#     for p in products:
#         if p["id"] == product_id:
#             products.remove(p)
#             return jsonify({"message": "Product deleted"}), 200
#     return jsonify({"error": "Product not found"}), 404

# if __name__ == "__main__":
#     app.run(debug=True)

import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows all origins — browser can now call your Flask API

@app.route("/futurama/info", methods=["GET"])
def get_futurama_info():
    response = requests.get("https://api.sampleapis.com/futurama/info")

    if response.status_code == 200:
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)

