from functools import reduce
# Reduce Function :-
'''
The reduce() function in Python is used to apply a function to the elements of an iterable(like a list or tuple) 
and reduce the iterable to a single cumulative value. 
Unlike map() and filter(),which return iterators, reduce() returns a single result.

Use it when you need to reduce a list of values into a single value by applying a binary operation
(like summing, multiplying, finding the maximum, etc.).
'''

'''
1. **Calculate sum of numbers**: Write a function that takes a list of numbers and returns the
sum of all the numbers.
'''

def sum_num(num1, num2):
    return num1 + num2

li = [1, 2, 3, 4, 5]
result = reduce(sum_num, li)
print(result)

li1 = [1, 2, 3, 4, 5, 6]
result = reduce(lambda x, y : x + y, li1)
print(result)

'''
2.**Calculate factorial of a number**: Write a function that takes a number and returns its factorial.
'''
def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0 or n == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))

number = 5
result = factorial(number)
print(result)


# Multiplying Numbers with reduce():-
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
result = reduce(multiply, numbers)
print(result)
