# https://github.com/kgriffinuf/lab10-KG-FC.git
# Partner 1: Kenneth Griffin
# Partner 2: Francisco Carmona


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

def div(a, b): 
	try:
		return b / a
	except ZeroDivisionError:
		raise ZeroDivisionError("Cannot divide by zero")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    try:
        return math.log(b, a)
    except ValueError as e:
        if a <= 0:
            raise ValueError("a cannot be less than zero")
        elif b <= 1 or b == 1:
            raise ValueError("b must be greater than one")
        else:
            raise e


def exp(a, b):
    return a ** b




