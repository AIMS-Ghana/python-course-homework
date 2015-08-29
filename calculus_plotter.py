#!/usr/bin/env python3

from numpy import gradient
from scipy.integrate import odeint

# I(x) = integral(f)
# dIdx = f(x) = ...some user defined f
# odeint wants f(I,x) to solve for I

def calc_all(f, rangex, ifxmin = 0):
    fx = f(rangex)
    return {
        'f'  : fx,
        'df' : gradient(fx),
        'If' : odeint(lambda y, x:f(x), 0, rangex)
    }

import matplotlib.pyplot as pyplot

def plot_all(f, rangex, ifxmin = 0):
    lines = calc_all(f, rangex, ifxmin)
    fx, = pyplot.plot(rangex, lines['f'], '-')
    df, = pyplot.plot(rangex, lines['df'], ":")
    If, = pyplot.plot(rangex, lines['If'], "--")
    pyplot.legend([fx, df, If],['function','derivative','integral'])
    pyplot.show()

if __name__ == "__main__":
    from numpy import linspace
    x = linspace(-5,5,10,endpoint=True)
    plot_all(lambda x:x, x)