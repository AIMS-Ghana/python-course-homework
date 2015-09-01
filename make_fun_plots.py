#!/usr/bin/python

import calculus_plotter
import fun_plots
import numpy as np

xs = np.linspace(-5, 5)

for f in fun_plots.funclist:
    calculus_plotter.somefunction(f, xs)
    ## do something with f