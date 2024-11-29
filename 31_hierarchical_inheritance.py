# Hierarchical inheritance
'''
in Hierarchical inheritance, more than one child class is derived from a single parent class.
In other words, we can say one parent class and multiple child classes.
'''


class A:
    def show(self):
        print("Class A")


class B(A):
    def display(self):
        print("Class B")


class C(A):
    def introduce(self):
        print("Class C")


obj_c = C()
obj_c.introduce()
obj_c.show()

obj_b = B()
obj_b.display()
obj_b.show()


# hierarchical inheritance example 2 :-
class Vehicle:
    def info(self):
        print("This is Vehicle")


class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)


class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)


obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')
