#!/usr/bin/python


import midpoint
import fun_plots
import calculus_plotter


def plot_function(x):
	calculus_plotter._plot(x)


if __name__ == "__main__":
	for func in fun_plots.funclist:
		plot_function(func)	
