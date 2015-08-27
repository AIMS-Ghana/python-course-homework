#!/usr/local/bin/python3

import bisection

def bisectf(x):
    return (x-1)*(x+10)**2

rangex = (0, 20)

print(bisection.root(bisectf, rangex))