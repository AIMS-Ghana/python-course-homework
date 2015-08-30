#!/usr/bin/python
from fun_plots import *
from visual import*
from visual.graph import*
def plot_graph(f,value_format):
	gd = gdisplay(x=0, y=0, width=1500, height=1500,
      		title='N vs. t', xtitle='x', ytitle='y',
      		foreground=color.black, background=color.black,
      		xmax=50, xmin=-50, ymax=5, ymin=-5)
	f1=gcurve(color=color.red)
	for x in value_format:
		f1.plot(pos=(x,f(x)))
	g1=gcurve(color=color.green)
	h=10e-10
	for x in value_format:
		g1.plot(pos=(x,float(f(x+h)-f(x))/h))
