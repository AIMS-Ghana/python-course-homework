#!/usr/bin/python3

import fun_plots as fplt
import fun_plots2 as fp
import calculus_plotter as cplt

for k in range(0,5):
	cplt.calculus_plotter(fplt.funclist[k])
	cplt.calculus_plotter(fp.funclist[k])
