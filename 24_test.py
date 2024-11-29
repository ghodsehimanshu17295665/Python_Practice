# # dict_1 = {
# #     "name": "test1",
# #     "age": 10
# # }

# # # result =
# # for key in dict_1.keys():
# #     print(key)


# # for value in dict_1.values():
# #     print(value)


# a = 'hello'
# print(id(a))
# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))
# print(id(a[3]))
# print(id(a[4]))

# print(':')
# b = 'hello '
# print(id(b))
# print(id(b[0]))
# print(id(b[1]))
# print(id(b[2]))
# print(id(b[3]))
# print(id(b[4]))


# Iterator ------------------
li1 = [10, 20, 30, 40, 50]
iterator = iter(li1)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print('--------------')


# Generator :- -----------------------------------------------------------
def simple_gen(num):
    for number in range(1, num+1):
        yield number

# for num in simple_gen(5):
#     print(num)


a = simple_gen(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print('--------------')
# Generator :- -----------------------------------------------------------


def count(num):
    while num > 0:
        yield num
        num = num - 1


number = count(5)
print(number)
for num in number:
    print(num)
