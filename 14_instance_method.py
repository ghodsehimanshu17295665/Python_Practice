#Class Method:- 
# 1. Instance Method:-
class Student:

    #constructor:-
    def __init__(self,name,age):
        #Instance Variable:-
        self.name = name
        self.age = age

    # instance method access instance variable:-
    def show(self):
        print("Name:", self.name, "Age:", self.age)


    # instance method to modify instance variable
    def update(self,age):
        self.age = age

#Create First object:-
ob1 = Student('Jessa',12)
# Call Instance method:-
ob1.show()

#create second object:-
kelly = Student("Kelly", 16)
# call instance method
kelly.show()

print(kelly.name)
print(kelly.age)

# Modify instance variables
kelly.update(18)
kelly.show()
