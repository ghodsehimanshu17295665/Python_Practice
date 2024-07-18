# 1.Write a lambda function that takes two numbers and returns their sum.
add = lambda num1, num2: num1 + num2
print(add(5, 6))


# 2.Write a lambda function that takes two numbers and returns the larger number.
large_number = lambda num1, num2: num1 if num1 > num2 else num2

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))

print(large_number(num1, num2))

# 3.Write a lambda function to convert all strings in a list to upper case using the map function.
strings = ['hello', 'world', 'python']
str_upper_case = list(map(lambda str: str.upper(), strings))
print(str_upper_case)

# 4.Write a lambda function to find the length of each string in a list using the map function.
strings = ['apple', 'banana', 'cherry']
str_length = list(map(lambda str: len(str), strings))
print(str_length)

# 5.Write a lambda function to reverse each string in a list using the map function.
strings = ['hello', 'world', 'python']
reverse_str = list(map(lambda str: str[::-1], strings))
print(reverse_str)
