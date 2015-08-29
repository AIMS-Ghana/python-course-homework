#!/usr/bin/env python3

import calculus_plotter, fun_plots

from numpy import linspace

rangex = linspace(-10,10,100,endpoint=True)

for f in fun_plots.funclist:
    calculus_plotter.plot_all(f,rangex)