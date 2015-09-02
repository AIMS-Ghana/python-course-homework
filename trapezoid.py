#!/usr/bin/python

def trapezoid(f, a, b, n):
    c = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*c)
    s += f(b)/2.0
    return s * c

print( trapezoid(lambda x:x**2, 5, 10, 100))
