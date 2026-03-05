import csv
import io
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory product storage
products = []

@app.route("/api/upload-products", methods=["POST"])
def upload_products():
    # Check if file is in request
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    # Check if file is a CSV
    if not file.filename.endswith(".csv"):
        return jsonify({"error": "Only CSV files are allowed"}), 400

    # Read file content
    content     = file.read().decode("utf-8")
    reader      = csv.DictReader(io.StringIO(content))

    total_rows     = 0
    products_added = 0
    failed_rows    = 0
    errors         = []

    for row in reader:
        total_rows += 1

        name  = row.get("name",  "").strip()
        price = row.get("price", "").strip()
        stock = row.get("stock", "").strip()

        # Validate name
        if not name:
            failed_rows += 1
            errors.append({"row": total_rows, "reason": "Name is empty", "data": dict(row)})
            continue

        # Validate price
        try:
            price = float(price)
            if price <= 0:
                raise ValueError
        except ValueError:
            failed_rows += 1
            errors.append({"row": total_rows, "reason": "Price must be a valid number greater than 0", "data": dict(row)})
            continue

        # Validate stock
        try:
            stock = int(stock)
            if stock < 0:
                raise ValueError
        except ValueError:
            failed_rows += 1
            errors.append({"row": total_rows, "reason": "Stock must be a valid integer >= 0", "data": dict(row)})
            continue

        # All valid — add to storage
        products.append({
            "id":    len(products) + 1,
            "name":  name,
            "price": price,
            "stock": stock
        })
        products_added += 1

    return jsonify({
        "total_rows":     total_rows,
        "products_added": products_added,
        "failed_rows":    failed_rows,
        "errors":         errors
    }), 200


@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products), 200


if __name__ == "__main__":
    app.run(debug=True)
