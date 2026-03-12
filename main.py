from flask import Flask, jsonify

app = Flask(__name__)

BOOKS = [
    {"id": 1, "title": "Clean Code",        "author": "Robert C. Martin", "genre": "Technology"},
    {"id": 2, "title": "Atomic Habits",     "author": "James Clear",       "genre": "Self-Help"},
    {"id": 3, "title": "The Pragmatic Programmer", "author": "David Thomas","genre": "Technology"},
    {"id": 4, "title": "Sapiens",           "author": "Yuval Noah Harari", "genre": "History"},
    {"id": 5, "title": "Deep Work",         "author": "Cal Newport",       "genre": "Self-Help"},
    {"id": 6, "title": "The Phoenix Project", "author": "Gene Kim", "genre": "Technology"},
    {"id": 7, "title": "The Lean Startup", "author": "Eric Ries", "genre": "Business"}
]

@app.route('/')
def home():
    return jsonify({
        "service": "Book Catalog API",
        "version": "3.0.0",
        "endpoints": ["/books", "/books/<id>"]
    })

@app.route('/books')
def get_books():
    return jsonify({
        "total": len(BOOKS),
        "books": BOOKS
    })

@app.route('/books/<int:book_id>')
def get_book(book_id):
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)