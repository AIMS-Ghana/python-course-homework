#!/usr/bin/python3

import bisection

def bisectf(x):
    return x**2-x-2

rangex = [0,2]

print(bisection.root(bisectf, rangex))
