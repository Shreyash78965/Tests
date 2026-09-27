# library.py


class Book:

    def __init__(self, title: str, isbn: str):
        self.title = title
        self.isbn = isbn
        self.is_checked_out = False


class Library:

    def __init__(self, max_borrow_limit: int = 3):
        self.books = {}  # ISBN -> Book
        self.borrowed_counts = {}  # user_id -> count
        self.max_borrow_limit = max_borrow_limit

    def add_book(self, book: Book):
        """Adds a book to the library catalog."""
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self.books[book.isbn] = book

    def check_out(self, isbn: str, user_id: str) -> bool:
        """Allows a user to check out a book if limits and availability allow."""
        if isbn not in self.books:
            raise KeyError("Book not found in library.")

        book = self.books[isbn]
        if book.is_checked_out:
            raise RuntimeError("Book is already checked out.")

        current_borrowed = self.borrowed_counts.get(user_id, 0)
        if current_borrowed >= self.max_borrow_limit:
            raise PermissionError(
                f"User {user_id} has reached the maximum borrow limit."
            )

        # Update state
        book.is_checked_out = True
        self.borrowed_counts[user_id] = current_borrowed + 1
        return True

    def return_book(self, isbn: str, user_id: str) -> bool:
        """Returns a borrowed book back to the library."""
        if isbn not in self.books:
            raise KeyError("Book not found in library.")

        book = self.books[isbn]
        if not book.is_checked_out:
            raise RuntimeError("Book was not checked out.")

        book.is_checked_out = False
        self.borrowed_counts[user_id] = max(
            0, self.borrowed_counts.get(user_id, 1) - 1
        )
        return True