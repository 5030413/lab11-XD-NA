# https://github.com/5030413/lab11-XD-NA
# Partner 1: Xinlin Du
# Partner 2: Natasha Antoniuk

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example

import math

def add(a, b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
        assert a==0, "ZeroDivisionError"
        return b / a
    except AssertionError as e:
        print(f"Assert: {e}")

def log(a,b):
    try:
        assert b>0 and a>1, "ValueError"
        return math.log(b,a)
    except AssertionError as e:
        print(f"Assert: {e}")

def exp(a,b):
    return a**b

def add(a, b): 
    return a + b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exponent(a, b):
    return a ** b



