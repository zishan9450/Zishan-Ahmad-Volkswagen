from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flaskuser:root@localhost/fsd"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    copies = db.Column(db.Integer)

with app.app_context():
    db.create_all()

# POST /books → Add a book
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    book = Book(
        title=data["title"],
        author=data["author"],
        copies=data["copies"]
    )
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book added", "id": book.id}), 201

# GET /books → List all books
@app.route("/books", methods=["GET"])
def list_books():
    books = Book.query.all()
    return jsonify([
        {"id": b.id, "title": b.title,
         "author": b.author, "copies": b.copies}
        for b in books
    ]), 200

# POST /books/<id>/borrow → Borrow a book (reduce copies by 1)
@app.route("/books/<int:book_id>/borrow", methods=["POST"])
def borrow_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    if book.copies == 0:
        return jsonify({"error": "No copies available"}), 400
    book.copies -= 1
    db.session.commit()
    return jsonify({
        "message": f"'{book.title}' borrowed successfully",
        "copies_remaining": book.copies
    }), 200

# GET /books/unavailable → Books with copies = 0
@app.route("/books/unavailable", methods=["GET"])
def unavailable_books():
    books = Book.query.filter_by(copies=0).all()
    return jsonify([
        {"id": b.id, "title": b.title, "author": b.author}
        for b in books
    ]), 200

if __name__ == "__main__":
    app.run(debug=True)
