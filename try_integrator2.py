#!/usr/bin/python

import numpy as np

import trapezoid

def intf(x):
    return np.exp(x)

rangex = np.linspace(0, 10, 100, endpoint=True)

out = "{} integration, e^x on ({},{}): {}\nelapsed: {}"

start = time.clock()
res = trapezoid.integrate(bisectf, rangex)
elapsed = time.clock() - start

print(out.format(
    "trapezoid",
    rangex[0], rangex[-1],
    res,
    elapsed
))

start = time.clock()
res = trapezoid.integrate(bisectf, rangex)
elapsed = time.clock() - start

print(out.format(
    "Trapezoid",
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
