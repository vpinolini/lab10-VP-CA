import math
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a
def logarithm(a,b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError
    return math.log(b,a)
def exponent(a,b):
    if a < 0 and b % 1 != 0:
        raise ValueError
    elif a = 0 and b <= 0:
        raise ValueError
    return a**b