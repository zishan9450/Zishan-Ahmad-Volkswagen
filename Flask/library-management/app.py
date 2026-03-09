from flask import Flask, render_template, request, redirect
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

# Display all books
@app.route("/")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)

# Add a book
@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            copies=int(request.form["copies"])
        )
        db.session.add(book)
        db.session.commit()
        return redirect("/")
    return render_template("add_book.html")

# Borrow a book
@app.route("/borrow/<int:book_id>")
def borrow_book(book_id):
    book = Book.query.get(book_id)
    if book and book.copies > 0:
        book.copies -= 1
        db.session.commit()
    return redirect("/")

# Unavailable books
@app.route("/unavailable")
def unavailable():
    books = Book.query.filter_by(copies=0).all()
    return render_template("unavailable.html", books=books)

@app.route("/clear")
def clear_books():
    Book.query.delete()
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
