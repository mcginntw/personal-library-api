class BookList:
    """A class representing a collection of books in a user's list"""

    def __init__(self):
        self.books = []

    def add_book(self, title, tags=[]):
        """
        Add a book with an optional list of tags.
        
        :param title: The title of the book.
        :type title: str
        :param tags: A list of tags associated with the book.
        :type tags: list
        """
        self.books.append({'title': title, 'tags': tags})
    
    def give_book_tag(self, title, tag):
        """
        Add a tag to a book.
        
        :param title: The title of the book to tag.
        :type title: str
        :param tag: The tag to add.
        :type tag: str
        """
        for book in self.books:
            if book['title'] == title:
                book['tags'].append(tag)
                break
    
    def view_books(self):
        """
        Print the list of books with their tags.
        """
        for book in self.books:
            print(f"Title: {book['title']}, Tags: {', '.join(book['tags'])}")
    
    def update_books_by_tag(self, tag):
        """
        Get a list of books filtered by a specific tag.

        :param tag: The tag to filter books by.
        :type tag: str
        :return: A list of books that have the specified tag.
        """
        return [book for book in self.books if tag in book['tags']]

    def remove_book(self, title):
        """
        Remove a book from the list by its title.

        :param title: The title of the book to remove.
        :type title: str
        """
        self.books = [book for book in self.books if book['title'] != title]