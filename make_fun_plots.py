#!/usr/bin/python

import fun_plots
import fun_plots2
import calculus_plotter


def plot_function(x):
	calculus_plotter._plot(x)


if __name__ == "__main__":
	for func in fun_plots.funclist:
		plot_function(func)
	for func2 in fun_plots2.funclist:
		plot_function(func2)	
	
