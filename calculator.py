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
	except:
		return ('ZeroDivisionError')

def log(a, b):
	try:
		x = math.log(b, a)
		if b <= 0 or a <= 1:
			raise ValueError("Invalid parameter")
	except ValueError as error:
		return ("Caught ValueError", str(error))

def exp(a, b): 
	return a ** b


