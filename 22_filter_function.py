# Filter() Function :-
'''
The filter() function is used to filter out items from an iterable based on a condition 
or predicate function that returns True or False.

Use it when you need to filter items out of a collection based on some criteria (condition).
'''

'''
1. **Filter even numbers**: Write a function that takes a list of numbers and returns a new list
containing only the even numbers.
'''

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x : x % 2 == 0, list_number)
print(list(result))

'''
2. **Filter odd numbers**: Write a function that takes a list of numbers and returns a new list
containing only the odd numbers.
'''
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x : x % 2 != 0, list_number)
print(list(result))

'''
3. **Filter positive numbers**: Write a function that takes a list of numbers and returns a new list
containing only the positive numbers.
'''
list_number = [1, 2, 3, 4, -5, -6, 7, -8, 9, -10]
result = filter(lambda x : x > 0, list_number)
print(list(result))

'''
4. **Filter prime numbers**: Write a function that takes a list of numbers and returns a new list
containing only the prime numbers.
'''
num = 10

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_numbers = filter_primes(input_numbers)
print(prime_numbers)


'''
5. **Filter palindromes**: Write a function that takes a list of strings and returns a new list
containing only the palindromic strings.
'''
def is_palindrome(s):
    return s == s[::-1]

def filter_palindromes(strings):
    return [s for s in strings if is_palindrome(s)]

input_strings = ["racecar", "hello", "level", "world", "radar", "python"]
palindromic_strings = filter_palindromes(input_strings)
print(palindromic_strings)
