class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        new_books = []
        for b in self.books:
            if b.title != book.title and b.author != book.author:
                new_books.append(b)
        self.books = new_books

    def search_books(self, search_string):
        search_string = search_string.lower()
        results = []
        for b in self.books:
            if search_string in b.title.lower() or search_string in b.author.lower():
                results.append(b)
        return results
