#!/usr/bin/python

import bisection

def bisectf(x):
    return (x-1)*(x+10)**2

rangex = (0, 20)

out = "{} root of (x-1)(x+10)^2 on ({},{}): {}"

print(out.format(
    "bisection",
    rangex[0], rangex[1],
    bisection.root(bisectf, rangex)
))

from scipy.optimize import brentq

print(out.format(
    "scipy",
    rangex[0], rangex[1],
    brentq(bisectf, rangex[0], rangex[1])
))

