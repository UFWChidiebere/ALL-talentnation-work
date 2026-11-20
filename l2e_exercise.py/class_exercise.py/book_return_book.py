class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.isbn = ISBN
        self.availability = True

    def borrow_book(self):
        if not self.availability:
            print("This book is not available")
            return
        self.availability = False
        print("Borrowed! Please return the book when you are done")

    def return_book(self):
        if self.availability:
            print("You can't return what you did not take")
            return
        self.availability = True
        print("Thank you for returning the book back!")

    def display_info(self):
        print(f"{self.title} by {self.author} with ISBN: ({self.isbn})")

class Member:
    def __init__(self, name, ID):
        self.name = name
        self.member_id = ID
        self.borrowed_books = []

    def borrow(self, book):
        if self.availability:
            book.borrow_book()
            self.borrowed_books.append(book)
            return
        print("This book is not available")

    def return_book(self, book):
        if not book.availability:
            book.return_book()
            self.borrowed_books.remove(book)
            return
        print("The book wasn't borrowed")

    def display_books(self):
        if len(self.borrowed_books) == 0:
            print("You have no book to return")
            return
        print(f"You have {len(self.borrowed_books)} books left to return")
        for book in self.borrowed_books:
            print(f"{book.title}")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        if book in self.books:
            print("This book is already available")
            return
        self.books.append(book)

    def add_members(self, member):
        if member in self.members:
            print("Member already availble")
            return
        self.members.append(member)

    def show_books(self):
        print("-----Books------")
        for book in self.book:
            print(f"{book.title} by {book.author}")

    def show_members(self):
        print("------Members------")
        for member in self.members:
            print(f"{member.name} ({member.member_id})")




        

