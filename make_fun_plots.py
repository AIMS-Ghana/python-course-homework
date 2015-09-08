#!/usr/bin/python
import fun_plots as fp
import calculus_plotter as cp
import fun_plot2 as fp2

for i in range(0,5):
    cp.fn_plotter(fp.funclist[i])
    cp.fn_plotter(fp2.funclist[i])

