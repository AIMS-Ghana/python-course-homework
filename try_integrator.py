#!/usr/bin/env python3
<<<<<<< Updated upstream

import numpy as np
import midpoint

def intf(x):
    return np.exp(x)

rangex = np.linspace(0, 10, 100, endpoint=True)

out = "{} integration, e^x on ({},{}): {}"

print(out.format(
    "midpoint",
    rangex[0], rangex[-1],
    midpoint.integrate(intf, rangex)
))

from scipy.integrate import quad

print(out.format(
    "scipy",
    rangex[0], rangex[-1],
    quad(intf, rangex[0], rangex[-1])
))
=======
import math
import sys
from scipy.integrate import quad

    
h = float(10)/10
    
  
    
sum = 0.0
x = h/2                  # first midpoint
while (x < 1):
	sum += h * math.exp(x)
	x += h 
	print (sum)
>>>>>>> Stashed changes
