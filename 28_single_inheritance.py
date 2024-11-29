# Single Inheritance :-
class A:
    def show(self):
        print("Class A")


class B(A):
    def display(self):
        print("Class B")


ob_b = B()
ob_b.display()
ob_b.show()


# Single Inheritance Exmple 2:-
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def child_1(self):
        return f"{self.name} Alice, {self.age} 4"


class Child(Parent):
    def child_2(self):
        return f"{self.name} Tom, {self.age} 2"


obj = Child("name : ", "age : ")
print(obj.child_1())
print(obj.child_2())
