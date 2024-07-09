# Python Function:-

#Creating a function:-
def my_function():
  print("Hello from a function") 
#Calling a Function:
my_function()

print('\n')

#Arguments:-
#Example:-1 -->
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print('\n')

#example:-2 -->
# A simple Python function to check whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
# Driver code to call the function
evenOdd(2)
evenOdd(3)

print('\n')

#Types of Python Function Arguments:-
# 1. Default Arguments:-

# Python program to demonstrate default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
# Driver code (We call myFun() with only argument)
myFun(10)

#Example:-2-->>
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

print('\n')
#2. Keyword Argument:-
#example:-1
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')


#3. Positional Arguments

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
# You will get correct output because 
# argument is given in order
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("Case-2:")
nameAge(27, "Suraj")

print('\n')
#4. Arbitrary Keyword  Arguments:-     
# 1. *args in Python (Non-Keyword Arguments)
# 2. **kwargs in Python (Keyword Arguments)

#*args (Positional Arguments):-
def my_function(*args):
    for i in args:
        print(i)
# Example usage:
my_function(1, 2, 3)

#**kwargs (Keyword Arguments):-
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Example usage:
my_function(name="Alice", age=30, city="New York")

#Using *args and **kwargs Together :-
def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# Example usage:
my_function(1, 2, 3, name="Alice", age=30)

print('\n')
#Anonymous Functions in Python(Lamda Function):-
# Python code to illustrate the cube of a number using lambda function
#Normal_Function:-
def cube(x):
    return x*x*x
print(cube(7))
#Using Lambda_Function:-
cube_v2 = lambda x : x*x*x
print(cube_v2(7))

print('\n')

#Recursive Functions in Python:
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))

print('\n')

#Return Statement in Python Function:-
def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))

print('\n')

#Pass by Reference and Pass by Value:-
# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20
# Driver Code (Note that lst is modified after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)
print(len(lst))


