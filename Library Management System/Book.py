
# -----------------------------
# Book class definition
# -----------------------------
class Book:
    # Constructor to set up book details when a Book object is created
    def __init__(self, book_id, title, author, quantity):
        # Unique ID for each book
        self.book_id = book_id
        # Book title (name of the book)
        self.title = title
        # Author name
        self.author = author
        # How many copies are available
        self.quantity = quantity

    # Function to show all details of a book
    def display_book_info(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Quantity: {self.quantity}")

    # Function to check if the book is available for borrowing
    def check_availability(self):
        # Returns True if quantity > 0, otherwise False
        return self.quantity > 0

    # Function to change the number of available copies
    # 'change' can be positive (returning a book) or negative (borrowing a book)
    def update_quantity(self, change):
        self.quantity += change
