#!/usr/bin/python
import calculus_plotter
import fun_plots


if __name__ == "__main__":
	for i in range(len(fun_plots.funclist)-1):
		calculus_plotter.plot_all(fun_plots.funclist[i])
	

