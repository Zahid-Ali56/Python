import pickle
from Book import Book
from User import User

class Library:
    def __init__(self):
        self.books = self.load_data("books.pkl")
        self.users = self.load_data("users.pkl")

        if not self.books:
            self.books = [
                Book(1, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 5),
                Book(2, "The Hobbit", "J.R.R. Tolkien", 3),
                Book(3, "1984", "George Orwell", 4),
                Book(4, "To Kill a Mockingbird", "Harper Lee", 2)
            ]
            self.save_data("books.pkl", self.books)

        if not self.users:
            self.users = [User(1, "Alice")]
            self.save_data("users.pkl", self.users)

    def add_book(self, book):
        self.books.append(book)
        self.save_data("books.pkl", self.books)
        print(f"Book '{book.title}' added and saved successfully!")

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display_book_info()

    def search_book_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def register_user(self, user):
        if any(u.user_id == user.user_id for u in self.users):
            print("User ID already exists!")
        else:
            self.users.append(user)
            self.save_data("users.pkl", self.users)
            print(f"User {user.name} registered successfully and saved!")

    def borrow_book(self, user_id, book_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if user and book:
            user.borrow_book(book)
            self.save_data("books.pkl", self.books)
            self.save_data("users.pkl", self.users)
        else:
            print("Invalid User ID or Book ID.")

    def return_book(self, user_id, book_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if user and book:
            user.return_book(book)
            self.save_data("books.pkl", self.books)
            self.save_data("users.pkl", self.users)
        else:
            print("Invalid User ID or Book ID.")

    def save_data(self, filename, data):
        with open(filename, "wb") as f:
            pickle.dump(data, f)

    def load_data(self, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def delete_book(self, book_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        if book:
            self.books.remove(book)
            self.save_data("books.pkl", self.books)
            print(f"Book ID {book_id} deleted successfully.")
        else:
            print("Book not found.")

    def delete_user(self, user_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if user:
            self.users.remove(user)
            self.save_data("users.pkl", self.users)
            print(f"User ID {user_id} deleted successfully.")
        else:
            print("User not found.")


def main():
    library = Library()

    while True:
        print("\n Library Management System ")
        print("1. View All Books")
        print("2. Add Book")
        print("3. Search Book by Title")
        print("4. Register User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Delete Book")
        print("8. Delete User")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.list_books()

        elif choice == '2':
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))
            library.add_book(Book(book_id, title, author, quantity))

        elif choice == '3':
            title = input("Enter Title to Search: ")
            results = library.search_book_by_title(title)
            if results:
                for book in results:
                    book.display_book_info()
            else:
                print("No matching books found.")

        elif choice == '4':
            user_id = int(input("Enter User ID: "))
            name = input("Enter User Name: ")
            library.register_user(User(user_id, name))

        elif choice == '5':
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID to Borrow: "))
            library.borrow_book(user_id, book_id)

        elif choice == '6':
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID to Return: "))
            library.return_book(user_id, book_id)

        elif choice == '7':
            book_id = int(input("Enter Book ID to delete: "))
            library.delete_book(book_id)

        elif choice == '8':
            user_id = int(input("Enter User ID to delete: "))
            library.delete_user(user_id)

        elif choice == '9':
            print(" Exiting... All data saved permanently. ")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
