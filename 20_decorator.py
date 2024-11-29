import copy
# # def fun():
# #     return 'a'


# # get = fun()
# # print(get)

# Generator :- 
# def count_down(num):
#     while num > 0:
#         yield num
#         num = num - 1


# values = count_down(5)
# for x in values:
#     print(x)



# list = [ x * x for x in range(100000000000000000000000000000)]

# for x in list:
#     print(x)


# # list1s  = ( x * x for x in range(10000000000000000000))
# # print(list1s)
# # for x in list1s:





# # Global namespace
# x = 10

# def outer_function():
#     # Enclosing namespace (for inner_function)
#     y = 20

#     def inner_function():
#         # Local namespace
#         z = 30
#         print("z (local):", z)
#         print("y (enclosing):", y)
#         print("x (global):", x)

#     inner_function()

# outer_function()

# print("x (global):", x)


# for i in range(1, 5):
#     for j in range(i*2-1):
#         print('*', end='')
#     print('')


# for i in range(1, 8, 2):
#     print('*' * i)


# for i in range(1, 6):
#     for k in range(1, 6-i):
#         print(' ', end='')
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print('')


for i in range(1, 6):
    print(' ' * (5 - i) + '* ' * i)





def wrapper(func):
    def inner(*args, **kwargs):
        return 2*func(*args, **kwargs)
    return inner


@wrapper
def double(a):
    return a


print(double(10))


numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[1:-1][::-1])


numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[1:5][::-1])

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# [70, 60, 50, 40, 30]
print(numbers[-2:-7:-1])

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# [80, 70, 60]
print(numbers[-1:-4:-1])
print(numbers[-1:])
print(numbers[:-4])


numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# Now, slice the list to get the first element and the fourth element together.
print([numbers[0], numbers[3]])

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
# Get the first 3 and last 2 elements
print(numbers[:3] + numbers[-2:])


# Generator :- -----------------------------------------------------------
def count(num):
    while num > 0:
        yield num
        num = num - 1


number = count(5)
for numbers in number:
    print(numbers)


# Example 1: Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for num in range(n):
        yield a
        a, b = b, a + b


number = fibonacci(7)
for num in number:
    print(num, end=' ')

print('\n')


def simple_generator(n):
    for num in range(n+1):
        yield num


for number in simple_generator(5):
    print(number)
print('\n')


x = 10
gen = (i for i in range(x) if i % 2 == 0)

lis = [i for i in range(x) if i % 2 == 0]

print(gen)
print(lis)
for num in gen:
    print(num)
print('\n')


# Iterator :---------------------------------------------
mylist = [1, 2, 3, 4, 5, 6, 7]
iterator = iter(mylist)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print('\n')

original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)
shallow_copied_list[2][0] = 'Changed'
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)


original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[2][0] = 'Changed'
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

print('\n')

original_value = [{'a': 3}, {'b': 4}, {'c': 7}, {'d': 1}]
deep_copy = copy.deepcopy(original_value)

original_value[2] = 5
original_value[0] = 9

print("original:", original_value)
print("deep:", deep_copy)
print('\n')


original_dict = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
shallow_copied_dict = copy.copy(original_dict)
original_dict['b'][0] = 99
original_dict['c']['d'] = 100
# original_dict['c'] = 'hello'
print(original_dict)
print(shallow_copied_dict)
