# Multiple Inheritance :-
'''
In multiple inheritance, one child class can inherit from multiple parent classes.
So here is one child class and multiple parent classes.
'''


class A:
    def show(self):
        print("Class A")


class B:
    def display(self):
        print("Class B")


class C(A, B):
    def introduce(self):
        print("Class C")


obj = C()
obj.introduce()
obj.display()
obj.show()


# Multiple Inheritance Example 2 :-
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"


class Pet:
    def __init__(self, owner):
        self.owner = owner

    def get_owner(self):
        return f"{self.owner} is the owner"


class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def bark(self):
        return f"{self.name} is barking"


dog = Dog("Shero", "Nick")
print(dog.eat())
print(dog.get_owner())
print(dog.bark())


# Multiple Inheritance Example 3 :-
# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)


# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)


# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)


# Create object of Employee
emp = Employee()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')
