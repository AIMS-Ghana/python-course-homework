#!/usr/bin/python

import fun_plots
import calculus_plotter


fun = fun_plots.funclist
for i in range (0,(len(fun)-1)):
	calculus_plotter.plotting(fun[i])
