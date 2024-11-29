# MRO - Method Resolution Order

# Example 1: Simple Single Inheritance
class A:
    def show(self):
        print("Class A")


class B(A):
    pass


class C(B):
    pass


obj_c = C()
obj_c.show()
print(C.mro())


# Example 2: Multiple Inheritance
class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")


class D(B, C):
    pass


obj_d = D()
obj_d.show()
print(D.mro())


# Example 3: Changing the Order of Inheritance
class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")


class D(C, B):
    pass


obj_d = D()
obj_d.show()
print(D.mro())


# Example 4: Multilevel Inheritance with Multiple Inheritance
class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")


class D(B):
    pass


class E(C):
    pass


class F(D, E):
    pass


obj_f = F()
obj_f.show()
print(F.mro())


# Example 5: Using super() with MRO
class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")
        super().show()


class C(A):
    def show(self):
        print("Class C")
        super().show()


class D(B, C):
    def show(self):
        print("Class D")
        super().show()


obj_d = D()
obj_d.show()
print(D.mro())
