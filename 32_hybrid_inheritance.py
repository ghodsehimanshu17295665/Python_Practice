# Hybrid Inheritance :-
'''
When inheritance is consists of multiple types or
a combination of different inheritance is called hybrid inheritance.
'''


class A:
    def show(self):
        print("Class A")


class B(A):  # Single Inheritance
    def display(self):
        print("Class B")


class C(A):  # Hierarchical Inheritance
    def introduce(self):
        print("Class C")


class D(B, C):  # Multiple Inheritance
    def announce(self):
        print("Class D")


# Creating an instance of D
obj_d = D()
obj_d.show()
obj_d.display()
obj_d.introduce()
obj_d.announce()


# Example - 2:-
class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")


class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")


# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")


# create object
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()
