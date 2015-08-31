#!/usr/bin/python

from numpy import *
from scipy.integrate import odeint


def calc_all(f, rangex, ifxmin = 0):
    fx = f(rangex)
    return {
        'f'  : fx,  #some user defined function
        'df' : gradient(fx), #the derivative of the function
        'If' : odeint(lambda y, x:f(x), 0, rangex) #intergral of the function
    }

import matplotlib.pyplot as plt

def plot_all(f, rangex, ifxmin = 0):
    lines = calc_all(f, rangex, ifxmin)
    fx, = plt.plot(rangex, lines['f'], '--')
    df, = plt.plot(rangex, lines['df'], ".")
    If, = plt.plot(rangex, lines['If'], "-")
    plt.legend([fx, df, If],['function','derivative','integral'])
    plt.show()

if __name__ == "__main__":
    from numpy import linspace
    x = arange(0,10,0.01)
    plot_all(lambda x:x, x)



