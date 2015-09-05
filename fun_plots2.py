
import numpy as np

def quadratic(x):
    return x**2

def simp_int(x):
    return 1 + 0.23**x

def comp_int(x):
    return (1 + 0.23)**x

def tanh(t):
    return np.tanh(t)

def log(t):
    return np.log(abs(t))

funclist = [
    quadratic, simp_int,
    comp_int, tanh,
    log
]