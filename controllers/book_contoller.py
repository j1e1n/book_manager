from flask import Flask, render_template
from flask import Blueprint 
books_blueprint = Blueprint("books", __name__)
from repositories import book_repository


@books_blueprint.route('/books', methods=['GET'])
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)