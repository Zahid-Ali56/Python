# class User:
#     def __init__(self, user_id, name):
#         self.user_id = user_id
#         self.name = name
#         self.borrowed_books = []
#
# def borrow_book(self, book):
#     if book.check_availability():
#         self.borrowed_books.append(book)
#         book.update_quantity(-1)
#         print(f"{self.name} borrowed '{book.title}'")
#     else:
#         print(f"'{book.title}' is not available.")
#
# def return_book(self, book):
#     if book in self.borrowed_books:
#         self.borrowed_books.remove(book)
#         book.update_quantity(1)
#         print(f"{self.name} returned '{book.title}'")
#     else:
#         print(f"{self.name} does not have '{book.title}' borrowed.")

# -----------------------------
# User class definition
# -----------------------------
class User:
    # Constructor to set up user details when a User object is created
    def __init__(self, user_id, name):
        # Unique ID for each user
        self.user_id = user_id
        # Name of the user
        self.name = name
        # List to keep track of books this user has borrowed
        self.borrowed_books = []

    # Function to borrow a book
    def borrow_book(self, book):
        # Check if the book is available in the library
        if book.check_availability():
            # Add the book to the user's borrowed list
            self.borrowed_books.append(book)
            # Reduce the quantity of that book in the library by 1
            book.update_quantity(-1)
            # Show confirmation message
            print(f"{self.name} borrowed '{book.title}'")
        else:
            # Show message if the book is not available
            print(f"'{book.title}' is not available.")

    # Function to return a borrowed book
    def return_book(self, book):
        # Check if the user actually borrowed the book
        if book in self.borrowed_books:
            # Remove the book from user's borrowed list
            self.borrowed_books.remove(book)
            # Increase the book's quantity by 1 (book returned)
            book.update_quantity(1)
            # Show confirmation message
            print(f"{self.name} returned '{book.title}'")
        else:
            # Show message if the user didn't borrow this book
            print(f"{self.name} does not have '{book.title}' borrowed.")
