# sample_28.py
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
