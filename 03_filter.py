# Filtering Even Numbers:-
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20]


def is_even(num):
    return num % 2 == 0

# Using filter to get even numbers


even_num = filter(is_even, numbers)
# Convert the filter object to a list
result = list(even_num)
print(result)


# Using Lambda Function:-
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda num: num % 2 == 0, list1))
print(result)


#  to filter out strings that contain the letter 'a':
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

words_with_a = list(filter(lambda word: 'a' in word, words))
print(words_with_a)

# 1.Given a list of integers, filter out only the positive numbers.
numbers = [-10, -5, 0, 5, 10, 15, -20, 25]

positive_int = list(filter(lambda num: num >= 0, numbers))
print(positive_int)

# 2.Given a list of strings, filter out the strings that are exactly 5 characters long.
words = ["hello", "world", "Python", "is", "great", "fun"]
five_char_str = list(filter(lambda word: len(word) == 5, words))
print(five_char_str)

# 3.Given a list of integers, filter out the numbers that are divisible by 3.
numbers = [3, 7, 9, 12, 18, 20, 21, 24, 25]
num_div = list(filter(lambda num: num % 3 == 0, numbers))
print(num_div)

# 4.Given a list of strings, filter out the strings that are palindromes 
words = ["madam", "racecar", "python", "level", "world", "radar"]
palindromes_str = list(filter(lambda word: word == word[::-1], words))
print(palindromes_str)
