#!/usr/local/bin/python3

import bisection
import secant

def bisectf(x):
    return (x-1)*(x+10)**2

rangex = (0, 20)

out = "{} root of (x-1)(x+10)^2 on ({},{}): {}\nelapsed: {}"

import time

start = time.clock()
res = bisection.root(bisectf, rangex)
elapsed = time.clock() - start

print(out.format(
    "bisection",
    rangex[0], rangex[1],
    res,
    elapsed
))

start = time.clock()
res = secant.root(bisectf, rangex)
elapsed = time.clock() - start

print(out.format(
    "bisection",
    rangex[0], rangex[1],
    res,
    elapsed
))

from scipy.optimize import brentq

start = time.clock()
res = brentq(bisectf, rangex[0], rangex[1])
elapsed = time.clock() - start

print(out.format(
    "scipy",
    rangex[0], rangex[1],
    res,
    elapsed
))