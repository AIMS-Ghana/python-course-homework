#!/usr/bin/env python

import numpy as np
import trapeziod

def intf(x):
    return np.exp(x)

rangex = np.linspace(0, 10, 100, endpoint=True)

out = "{} integration, e^x on ({},{}): {}"

print(out.format(
<<<<<<< HEAD
    "trapeziod",

    rangex[0], rangex[-1],
    trapeziod.integrate(intf, rangex)
))

from scipy.integrate import quad

print(out.format(
    "scipy",
    rangex[0], rangex[-1],
    quad(intf, rangex[0], rangex[-1])
))
