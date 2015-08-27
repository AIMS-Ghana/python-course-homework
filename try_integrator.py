#!/usr/bin/python3

import midpoint

def intf(x):
    return x-x**2

rangex = [0,1]

print(midpoint.integrate(intf, rangex))
