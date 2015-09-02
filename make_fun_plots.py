#!/usr/bin/env python

import calculus_plotter
import fun_plots


for i in range(0,5):
    calculus_plotter.fplot(fun_plots.funclist[i],i)

