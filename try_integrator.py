#!/usr/local/bin/python3

import numpy as np
import midpoint

def intf(x):
    return np.exp(x)

rangex = np.linspace(0, 10, 100, endpoint=True)

print(midpoint.integrate(intf, rangex))