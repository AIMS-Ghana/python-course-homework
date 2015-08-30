#!/usr/bin/python
import calculus_plotter
import fun_plots


if __name__ == "__main__":
	for i in range(len(fun_plots.funclist)-1):
		calculus_plotter.main(fun_plots.funclist[i])
	

