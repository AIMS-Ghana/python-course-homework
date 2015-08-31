#!/usr/bin/env python3

import numpy as np
import midpoint
import trapezoid
import time

def intf(x):
    return np.exp(x)

rangex = np.linspace(0, 10, 100, endpoint=True)

out = "{} integration, e^x on ({},{}): {}\nelapsed: {}"

start = time.clock()
res = midpoint.integrate(intf, rangex)
elapsed = time.clock() - start

print(out.format(
    "midpoint",
    rangex[0], rangex[-1],
    res,
    elapsed
))

start = time.clock()
res = trapezoid.integrate(intf, rangex)
elapsed = time.clock() - start

print(out.format(
    "trapezoid",
    rangex[0], rangex[-1],
    res,
    elapsed
))

from scipy.integrate import quad

start = time.clock()
res = quad(intf, rangex[0], rangex[-1])
elapsed = time.clock() - start

print(out.format(
    "scipy",
    rangex[0], rangex[-1],
    res,
    elapsed
))
