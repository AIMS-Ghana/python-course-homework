#!/usr/bin/python
import calculus_plotter
import fun_plots
from visual import*
from visual.graph import*
v=arange(-5,5,0.1)
calculus_plotter.plot_graph(fun_plots.exp_growth,v)
calculus_plotter.plot_graph(fun_plots.exp_saturation,v)
