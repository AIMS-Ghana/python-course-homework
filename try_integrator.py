#!/usr/bin/python3
import numpy as np
import midpoint

def intf(x):
    return x-x**2

rangex = np.linspace(0,1,100)

print(midpoint.integrate(intf, rangex))
