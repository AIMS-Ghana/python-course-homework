#!/usr/bin/env python3

import numpy as np
import midpoint
import Trapezoidal

def intf(x):
    return np.exp(x)

rangex = np.linspace(0, 10, 100, endpoint=True)

out = "{} integration, e^x on ({},{}): {}"

print(out.format(
    "midpoint",
    rangex[0], rangex[-1],
    midpoint.integrate(intf, rangex)
))

print(out.format(
    "Trapezoidal",
    rangex[0], rangex[-1],
    Trapezoidal.integrate(intf, rangex)
))

from scipy.integrate import quad

print(out.format(
    "scipy",
    rangex[0], rangex[-1],
    quad(intf, rangex[0], rangex[-1])
))
