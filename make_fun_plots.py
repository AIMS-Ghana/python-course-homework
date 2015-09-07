#!/usr/bin/env python

import calculus_plotter
import fun_plots
import fun_plots2

for i in range(0,5):
    calculus_plotter.fplot(fun_plots.funclist[i],i)
    #calculus_plotter.fplot(fun_plots2.funclist[i],i)


