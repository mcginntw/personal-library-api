class BookList:
    """A class representing a collection of books in a user's list"""

    def __init__(self):
        self.books = []

    def add_book(self, title, tags=[]):
        """Add a book with an optional list of tags."""
        self.books.append({'title': title, 'tags': tags})

    def update_book_tags(self, title, tags):
        """Replace tags for a specific book."""
        for book in self.books:
            if book['title'] == title:
                book['tags'] = tags
                break

    def view_books(self):
        """Print the list of books with their tags."""
        for book in self.books:
            print(f"Title: {book['title']}, Tags: {', '.join(book['tags'])}")
    
    def search_books_by_title(self, search_term):
        """Search books by title."""
        return [book for book in self.books if search_term.lower() in book['title'].lower()]

    def update_books_by_tag(self, tag):
        """Get a list of books filtered by a specific tag."""
        return [book for book in self.books if tag in book['tags']]

    def remove_book(self, title):
        """Remove a book from the list by its title."""
        self.books = [book for book in self.books if book['title'] != title]
