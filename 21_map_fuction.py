# Map() Function :-
'''
map() function in python is used to apply a function to all items in an iterable like(list, tuple etc)
and return map objects (which is an iterator).

Use it when you want to transform or change each element in an iterable in a specific way.
'''

'''
1.Square each element: Write a function that takes a list of numbers and returns a new list
where each element is the square of the corresponding element in the input list.
'''
def square(num):
    return num ** 2
num = [1, 2, 3, 4, 5, 6]
result = map(square, num)
print(list(result))

# Using Lambda Function :-
num = [11, 12, 13, 14, 15, 16]
result = list(map(lambda X: X ** 2, num))
print(result)


'''
2.**Convert Strings to Uppercase**: Write a function that takes a list of strings and returns a
new list where each string is converted to uppercase.
'''
def str_upper(n):
    return n.upper()

str_list = ['hello', 'python', 'together', 'everyone', 'achieves', 'more']
result = map(str_upper, str_list)
print(list(result))

# Using lamvda Function :- 
list_str = ['hello', 'python', 'together', 'everyone', 'achieves', 'more']
result = list(map(lambda x: x.upper(), list_str))
print(result)

'''
3. **Calculate Length of Strings**: Write a function that takes a list of strings and returns a new
list where each element is the length of the corresponding string in the input list.
'''
def str_len(n):
    return len(n)

str_list = ['hello', 'python', 'together', 'everyone', 'achieves', 'more']
result = map(str_len, str_list)
print(list(result))

# Using lambda :-
list_str1 = ['hello', 'python', 'together', 'everyone', 'achieves', 'more']
result = list(map(lambda x: len(x), list_str1))
print(result)

'''
4. **Remove Leading Zeros from Strings**: Write a function that takes a list of strings
representing numbers and returns a new list where leading zeros are removed from each string.
'''
def remove_leading_zeros(strings):
    return list(map(lambda x: str(int(x)) if x != '0' else '0', strings))

# Example usage
input_strings = ["00123", "0456", "000789", "1000", "0000", "42"]
output_strings = remove_leading_zeros(input_strings)
print(output_strings)

'''
5. **Check if Numbers are Even**: Write a function that takes a list of numbers and returns a
new list where each element is True if the corresponding number in the input list is even, and
False otherwise.
'''
def even_odd(num):
    return num % 2 == 0

a = [1, 2, 3, 4, 5, 6, 7, 8]
result = map(even_odd, a)
print(list(result))

# Using lambda :-
a = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x % 2 == 0, a))
print(result)

'''
6. **Calculate Factorial of Numbers**: Write a function that takes a list of numbers and returns
a new list where each element is the factorial of the corresponding number in the input list.
'''
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num-1)

number = 5
print(fact(number))


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

list_number = [2, 3, 4, 5, 6, 7]
result = map(fact, list_number)
print(list(result))
