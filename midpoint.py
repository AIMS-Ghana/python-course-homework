#!/usr/bin/python

from scipy import *
from numpy import *
def f(x):
    return e**x

def integLeft(a, b, f, bins=10):
    h = float((b-a)/bins)
    assert h > 0
    assert type(bins) == int

    sum = 0.0
    for n in range(bins):
        sum = sum + h * f(a + n*h)
    return sum

def integMid(a, b, f, bsin=10):
    h = float((b-a)/bins)
    assert h > 0
    assert type(bins) == int

    sum = 0.0
    x = a + h/2
    while (x < b):
        sum = h * f(x)
        x = h

    return sum

if __name__ =="__main__":

    print(integLeft(a, b, f, bins=10))

