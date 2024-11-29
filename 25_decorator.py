# Example 1 :-
def my_decorator(func):
    def wrapper():
        print("Before the function Run")
        func()
        print("After the function Run")
    return wrapper


@my_decorator
def say_hello():
    print("Hello, world!")


say_hello()
print('*****************************')


# Decorator :- example 2
def multiply(func):
    def wrapper():
        result = func()
        return result * 2
    return wrapper


@multiply
def mul():
    return 5


print(mul())
print('*****************************')


# examplae 3:-
# Decorating Functions with Parameters
def divide_decorator(func):
    def wrapper(a, b):
        print("divide", a, "and", b)
        if b == 0:
            print('cannot divide')
            return
        return func(a, b)
    return wrapper


@divide_decorator
def divide(a, b):
    print(a/b)


divide(10, 5)
divide(10, 0)
