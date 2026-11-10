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

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a+b

def mul(a,b):
    return a*b

def div(a,b):
    try:
        assert a==0
        return b / a
    except ZeroDivisionError as e:
        print(f"Assert: {e}")

def exp(a,b):
    return a**b


def subtract(a, b):
    return a-b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)


