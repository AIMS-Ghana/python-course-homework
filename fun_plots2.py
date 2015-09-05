#!/usr/bin/env python 

import numpy as np

def easy(x):
    return x

def exp_saturation(x):
    return 1 - np.exp(-x-1)

def exp_growth(x):
    return np.exp(x)

def sine_and_cos(t):
    return np.cos(t) + np.cos(t)

def sine_sq(t):
    return np.sin(t)**2

funclist = [
    easy, exp_saturation,
    exp_growth, sine_and_cos,
    sine_sq
]
