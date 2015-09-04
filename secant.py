#!/usr/bin/env python3


def xn(f, x1, x2):
    return x2 - f(x2) * (x2 - x1) / ( f(x2) - f(x1) )


def root(f, rangex):
    tol = 10**(-8)
    x1, x2 = rangex[0], rangex[ len(rangex) - 1]
    x3 = xn(f, x1, x2)
    while abs(f(x3)) >= tol:
        print(x1,x2,x3)
        x4 = xn(f, x1, x2)
        x1 = x2
        x2 = x3
        x3 = x4
    return x3
