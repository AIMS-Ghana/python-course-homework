#!/usr/bin/env python
import fun_plots as fp
import fun_plots2 as fp2
import calculus_plotter as cp

for i in range (0,5):
	cp.plotter(fp.funclist[i])
 	cp.plotter(fp2.func_list[i])
