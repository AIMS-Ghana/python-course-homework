#!/usr/bin/python
import matplotlib.pyplot as plt
import calculus_plotter, fun_plots 

from numpy import linspace

x=linspace(-10,10,100,endpoint=True)
funclist = [
    easy, exp_saturation,
    exp_growth, sine_and_cos,
    sine_sq
]
plt.plot(funclist,x)
plt.show()





