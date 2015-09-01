#!/usr/bin/env python
import numpy as np
y=1
def easy(y):
   x=3*y**2-5*y
   return x

def exp_saturation(x):
    return 1 - np.exp(-x)

def exp_growth(x):
    return np.exp(5*x)

def sine_and_cos(t):
    return np.sin(t) + np.cos(t)

def sine_sq(t):
    return np.sin(t)**2

funclist = [
    easy, exp_saturation,
    exp_growth, sine_and_cos,
    sine_sq
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
]
=======
    print ("hello world")
>>>>>>> Stashed changes
=======
    print ("hello world")
>>>>>>> Stashed changes
=======
    print ("hello world")
>>>>>>> Stashed changes
