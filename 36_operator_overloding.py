# Operator Overloading :-

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __eq__(self, other):
        # Overloads the `==` operator to compare pages
        return self.pages == other.pages

    def __lt__(self, other):
        # Overloads the `<` operator to compare pages
        return self.pages < other.pages


book1 = Book("Python Basics", 350)
book2 = Book("Advanced Python", 500)

print(book1 == book2)  # Output: False, because 350 != 500
print(book1 < book2)   # Output: True, because 350 < 500


# Example 2: Adding Custom Objects (__add__)
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Define how the `+` operator works
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: Vector(6, 8)


# Example 3
# Python Program illustrate how
# to overload an binary + operator
# And how it actually works
class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1, ob2))
print(A.__add__(ob3, ob4))
# And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))
