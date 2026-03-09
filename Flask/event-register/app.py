# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flaskuser:root@[::1]/fsd"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    total_seats = db.Column(db.Integer)
    available_seats = db.Column(db.Integer)

class Registration(db.Model):
    __tablename__ = "registrations"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))

with app.app_context():
    db.create_all()

# POST /events → Create an event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    event = Event(
        name=data["name"],
        total_seats=data["total_seats"],
        available_seats=data["total_seats"]   # initially all seats available
    )
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": "Event created", "id": event.id}), 201

# GET /events → List all events
@app.route("/events", methods=["GET"])
def list_events():
    events = Event.query.all()
    return jsonify([
        {"id": e.id, "name": e.name,
         "total_seats": e.total_seats,
         "available_seats": e.available_seats}
        for e in events
    ]), 200

# POST /register/<event_id> → Register a user
@app.route("/register/<int:event_id>", methods=["POST"])
def register(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404
    if event.available_seats == 0:
        return jsonify({"error": "No seats available"}), 400
    data = request.get_json()
    reg = Registration(user_name=data["user_name"], event_id=event_id)
    event.available_seats -= 1
    db.session.add(reg)
    db.session.commit()
    return jsonify({"message": "Registered successfully",
                    "available_seats_left": event.available_seats}), 201

# GET /events/full → Events with no seats left
@app.route("/events/full", methods=["GET"])
def full_events():
    events = Event.query.filter_by(available_seats=0).all()
    return jsonify([
        {"id": e.id, "name": e.name, "total_seats": e.total_seats}
        for e in events
    ]), 200

if __name__ == "__main__":
    app.run(debug=True)
