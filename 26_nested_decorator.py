# Example :- 1
def decorator1(func):
    def wrapper():
        print('Decorator 1 before')
        func()
        print('Decorator 1 after')
    return wrapper


def decorator2(func):
    def wrapper():
        print('Decorator 2 before')
        func()
        print('Decorator 2 after')
    return wrapper


@decorator1
@decorator2
def say_hello():
    print('Hello')


say_hello()

print('**************************')
# Example :- 2


def greet(func):
    def wrapper():
        print("hello")
        return func()
    return wrapper


def exclaim(func):
    def wrapper():
        result = func()
        return result + '!!!'
    return wrapper


@greet
@exclaim
def say_name():
    return "jack"


print(say_name())
print('**************************')
# Example 3 :-


def decorator1(func):
    def wrapper(name):
        print('Decorator 1 : Welcome')
        func(name)
        print('Decorator 1 : Have a great day!')
    return wrapper


def decorator2(func):
    def wrapper(name):
        print('Decorator 2 : Starting the greeting...')
        func(name)
        print('Decorator 2: Greeting finished.')
    return wrapper


@decorator1
@decorator2
def greeting(name):
    print(f'Hello, {name}!')


greeting('John')




# Book.objects.aggregate(book_count=Count('book_name'))
