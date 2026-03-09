from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flaskuser:root@localhost/fsd"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

with app.app_context():
    db.create_all()

# POST /orders → Add an order
@app.route("/orders", methods=["POST"])
def add_order():
    data = request.get_json()
    order = Order(
        product_name=data["product_name"],
        quantity=data["quantity"],
        price=data["price"]
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({
        "message": "Order added",
        "id": order.id,
        "revenue": order.quantity * order.price
    }), 201

# GET /orders → All orders with per-order revenue
@app.route("/orders", methods=["GET"])
def list_orders():
    orders = Order.query.all()
    return jsonify([
        {"id": o.id, "product_name": o.product_name,
         "quantity": o.quantity, "price": o.price,
         "revenue": o.quantity * o.price}
        for o in orders
    ]), 200

# GET /orders/total-revenue → Total revenue using func.sum
@app.route("/orders/total-revenue", methods=["GET"])
def total_revenue():
    # Using SQLAlchemy aggregate as taught in class
    result = db.session.query(
        func.sum(Order.price * Order.quantity)
    ).scalar()
    return jsonify({"total_revenue": result or 0}), 200

# GET /orders/high-revenue → Orders where revenue > 2000
@app.route("/orders/high-revenue", methods=["GET"])
def high_revenue_orders():
    orders = Order.query.all()
    filtered = [
        {"id": o.id, "product_name": o.product_name,
         "quantity": o.quantity, "price": o.price,
         "revenue": o.quantity * o.price}
        for o in orders if o.quantity * o.price > 2000
    ]
    return jsonify(filtered), 200

if __name__ == "__main__":
    app.run(debug=True)
