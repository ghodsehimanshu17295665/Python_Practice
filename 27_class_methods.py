class Book:
    # Class attribute (shared by all instances)
    book_type = "Printed"

    def __init__(self, title, author, price):
        # Instance attributes
        self.title = title
        self.author = author
        self.price = price

    # Instance method
    def get_book_info(self):
        return f"'{self.title}' by {self.author}, priced at ${self.price}"

    # Class method
    @classmethod
    def set_book_type(cls, new_type):
        cls.book_type = new_type  # Modifies class attribute for all instances

    # Static method
    @staticmethod
    def is_valid_price(price):
        # Validates if price is a positive number
        return price > 0


# Creating an instance of Book
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)

# Using instance method
print(book1.get_book_info())

# Using class method to change book type for all books
Book.set_book_type("E-book")
print(Book.book_type)

# Using static method to check if a price is valid
print(Book.is_valid_price(15))
print(Book.is_valid_price(-5))
