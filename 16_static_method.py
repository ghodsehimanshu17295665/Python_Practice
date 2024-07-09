# Class Method:- 3 type of Methods in class
# 3. Static Method:-

class Employee:
    @staticmethod
    def sample(x):
        print("Inside Static Method",  x)
    
# call static method
Employee.sample(10)

# can be called using object
emp = Employee()
emp.sample(10)