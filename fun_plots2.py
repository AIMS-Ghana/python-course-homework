
import numpy as np

def easy_2(z):
    return (z+2)**2

def exp_saturation(x):
    return 1 - np.exp(-x)

def exp_growth(x):
    return np.exp(5*x)

def cos_sq(t):
    return np.cos(t)**2

def sine_sq(t):
    return np.sin(t)**2

funclist = [
    easy_2, exp_saturation,
    exp_growth, cos_sq,
    sine_sq
]
