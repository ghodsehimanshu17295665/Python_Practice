# Super Function :-
'''
super() is a built-in function that allows access to methods
and properties of a parent or superclass from a child or subclass.
'''


class A:
    def show(self):
        print("Class A - Show Method")


class B(A):
    def show(self):
        # Calls the show method of class A
        super().show()
        print("Class B - Show Method")


obj_b = B()
obj_b.show()
