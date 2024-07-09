# Class Method:- 3 type of Methods in class
# 2. Class method:-

class Student:
    # Class variable:-
    school_name = "ABC School"

    # Constructor:-
    def __init__(self,name,age):
        #Instace Variable:-
        self.name = name
        self.age = age
    
    #class method:-
    @classmethod
    def change_school(cls,school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # Instance method:-
    def show(self):
        print(self.name, self.age, 'School:',Student.school_name)

# Create object:-
ob1 = Student("jessa", 23)
ob1.show()

#Change School Name:-
Student.change_school("XYZ School")
ob1.show()