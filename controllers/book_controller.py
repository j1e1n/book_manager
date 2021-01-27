from flask import Flask, render_template, redirect
from flask import Blueprint 
books_blueprint = Blueprint("books", __name__)
from repositories import book_repository


@books_blueprint.route('/books', methods=['GET'])
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)


@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')


@books_blueprint.route('/books/<id>', methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book=book)

