#!/usr/bin/python
import calculus_plotter
from fun_plots import*
from visual import*
from visual.graph import*
v=arange(-10,10,0.01)
for x in funclist:
	calculus_plotter.plot_graph(x,v)
