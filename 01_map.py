# 1.Function to apply :-


def square(num):
    return num * num


num = [2, 3, 4, 5, 6]

square_number = map(square, num)

print(list(square_number))


# 2.Using lambda Function:-
numbers = [6, 7, 8, 9, 10]
square_number = map(lambda number: number * number, numbers)
print(list(square_number))


# 3.Multiple Iterables:-
number1 = [1, 2, 3]
number2 = [4, 5, 6]

sum_number = map(lambda num1, num2: num1 + num2, number1, number2)
print(list(sum_number))


# 4.Find the Length of Each String:
# Write a function that takes a list of strings and returns a list containing the length of each string.

def string_length(list1):
    return list(map(len, list1))


print(string_length(['apple', 'banana', 'cherry', 'orange']))


# 5.Define a function that doubles even numbers and leaves odd numbers as is

def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num


numbers = [1, 2, 3, 4, 5]

result = list(map(double_even, numbers))
print(result)
