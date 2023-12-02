#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        assert isinstance(page_count, int), "page_count must be an integer"
        self.title = title
        self.page_count = page_count

# Example usage:
if __name__ == "__main__":
    # Creating instances of the Book class
    book1 = Book("The Great Gatsby", 180)
    book2 = Book("To Kill a Mockingbird", 281)

    # Accessing and printing attributes
    print(book1.title)  # Output: The Great Gatsby
    print(book1.page_count)  # Output: 180

    print(book2.title)  # Output: To Kill a Mockingbird
    print(book2.page_count)  # Output: 281

    # Creating a Book instance with a non-integer page_count (will raise an AssertionError)
    try:
        invalid_book = Book("Invalid Book", "Not an Integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    
        