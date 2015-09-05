#!/usr/bin/python3

import matplotlib.pyplot as pyplot
from numpy import gradient
from scipy.integrate import odeint

def f_dif_int(f,rangex):
    values = f(rangex)
    return {
        'f' : values,
        'df': gradient(values),
        'If': odeint(lambda y,x :f(x),0, rangex)
    }


def plotter(f, rangex):
    graphs = f_dif_int(f, rangex)
    y, = pyplot.plot(rangex, graphs['f'], '-')
    df, = pyplot.plot(rangex, graphs['df'], ':')
    If, = pyplot.plot(rangex, graphs['If'], '--')
    pyplot.legend([y, df, If],['function','derivative','integral'])
    pyplot.show()

