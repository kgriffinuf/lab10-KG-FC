"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
	return a + b

def sub(a, b): 
	return a - b

def mul(a, b): 
	return a * b

def div(a, b): 
	try:
		return b / a
	except ZeroDivisionError:
		raise ZeroDivisionError("Cannot divide by zero")

def log(a, b):
    try:
        return math.log(b, a)
	except ValueError as error:
        if b <= 0:
            raise ValueError("Cannot logarithm of zero")
        if a <= 1:
            raise ValueError("Invalid parameter")
        else:
            raise error

def exp(a, b): 
	return a ** b

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




