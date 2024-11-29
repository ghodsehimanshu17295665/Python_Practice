# #Python Classes and Objects
# class Person:

#     def __init__(self, name, profession):
#         #Instance Variable (Data Memeber)
#         self.name = name
#         self.profession = profession

#     #instance Method:-
#     def show(self):
#         print("Name: ",self.name, "Profession: ",self.profession)
    
#     #instance Method :-
#     def work(self):
#         print(self.name, 'working as a', self.profession)

# # Create object of a class:-
# jessa = Person('Jessa', 'Software Engineer')
# #call Method:-
# jessa.show()
# jessa.work()

# print("\n")
# # Example :- 2 :-

# class Student:
#     #class variable
#     school_name = "ABC School"

#     #Constructor:-
#     def __init__(self,name,age):
#         #Instance Variable:-
#         self.name = name
#         self.age = age

# # Create object of a class:-
# s1 = Student("Ajay",8)

# # Access instance Variable:-
# print("Student: ", s1.name, s1.age)
# # Access class Variable:-
# print("School Name: ", Student.school_name)

# # Modify instance variables
# s1.name = 'Jessa'
# s1.age = 14
# print('Student:', s1.name, s1.age)
# # Modify class variables
# Student.school_name = 'XYZ School'
# print('School name:', Student.school_name)

class Parent1:

    def method1(self):
        pass


class Parent2:
    def method1(self):
        print("parent2")


class Child(Parent2, Parent1):
    pass


# Create an instance of Child
child = Child()
child.method1()


# MRO method resolution order

# multiple inheritance cyclic order child(left to right)

print(Child.mro())
