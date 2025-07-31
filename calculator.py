"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# KG code 559pm
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        if a < 0:
            raise ValueError("a must be greater than Zero")

def hypotenuse(a, b):
        return math.hypot(a, b)


# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by Zero")

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError as e:
        if a <= 0:
            raise ValueError("a cannot be less than zero")
        elif b <= 1 or b == 1:
            raise ValueError("b must be greater than one")
        else:
            raise e


def exp(a, b):
    return a ** b




