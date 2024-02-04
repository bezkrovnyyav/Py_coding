"""
Task:

Develop a book library management system using object-oriented programming (OOP) in Python. Implement classes for books, the library, customers, and the library management system. Consider the quantity of each book in the library.

Class Book:

Attributes: title (book title), author (author), year (publication year), quantity (number of copies of the book in the library, default is 1).

Method display_info, which prints information about the book.

Class EBook:

Inherits from the Book class.

Attribute: format_type (format of the electronic book, e.g., PDF).

Overrides the display_info method to print additional information about the electronic book format.

Class Library:

Attributes: books (list of books in the library), book_count (total number of books in the library).

Method add_book, which adds a new book to the library and increments book_count.

Method display_books, which prints the list of all books in the library.


Class Customer:

Attributes: name (customer name), borrowed_books (list of borrowed books).

Method borrow_book, allowing the customer to borrow a book from the library.

Method return_book, allowing the customer to return a borrowed book.


Class LibraryManagementSystem:

Attributes: library (object of the Library class), customers (list of customers).

Method register_customer, which adds a new customer to the system.

Method display_customer_books, which prints the list of books borrowed by a specific customer.

Method display_all_books, which prints the list of all books in the library.
"""
class Book:
    def __init__(self, title, author, year, quantity=1):
        self.title = title
        self.author = author
        self.year = year
        self.quantity = quantity

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}"

    def __str__(self):
        return self.display_info()

    def __repr__(self):
        return self.display_info()


class EBook(Book):
    def __init__(self, title, author, year, format_type, quantity=1):
        super().__init__(title, author, year, quantity)
        self.format_type = format_type

    def display_info(self):
        return super().display_info() + f" Format: {self.format_type}"

    def __str__(self):
        return self.display_info()

    def __repr__(self):
        return self.display_info()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Books in the Library:")
        for book in self.books:
            print(book)

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


class Customer:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book and book.quantity > 0:
            self.borrowed_books.append(book)
            book.quantity -= 1
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Book '{book.title}' is not available for borrowing.")

    def return_book(self, book, library=Library() ):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.books.append(book)
            book.quantity += 1
            print(f"{self.name} returned '{book.title}'.")
            return
        print(f"{self.name} did not borrow '{book.title}'.")
    
    def __str__(self):
        return f"{self.name} borrowed books:{self.borrowed_books}"


class LibraryManagementSystem:
    def __init__(self):
        self.library = Library()
        self.customers = []

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} registered in the system.")

    def display_customer_books(self, customer):
        print(f"Books borrowed by {customer.name}:")
        for book in customer.borrowed_books:
            print(book)

    def display_all_books(self):
        self.library.display_books()


library_system = LibraryManagementSystem()

customer1 = Customer("Alice")
customer2 = Customer("Bob")

book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
ebook1 = EBook("Python Crash Course", "Eric Matthes", 2015, "PDF")
ebook2 = EBook("Dive into Python 3", "Mark Pilgrim", 2009, "EPUB")


library_system.library.add_book(book1)
library_system.library.add_book(book2)
library_system.library.add_book(ebook1)
library_system.library.add_book(ebook2)


# Test data
	
# customer1 = Customer("Alice")
# customer2 = Customer("Bob")
# print(customer1)
# print(customer2)

	
# customer1.borrow_book(book1)
# customer1.borrow_book(ebook1)
# customer2.borrow_book(book2)

# library_system.display_customer_books(customer1)
# library_system.display_all_books()

	
# customer1.return_book(book1)
# customer2.return_book(book1)

# library_system.display_customer_books(customer1)
# library_system.display_all_books()