#!/usr/bin/python3

# Obtain test functions to plot on a diagram.
import fun_plots
import calculus_plotter
from numpy import linspace

rangex = linspace(-10,20,100, endpoint = True)


for f in fun_plots.funclist:
    calculus_plotter.plotter(f, rangex)

