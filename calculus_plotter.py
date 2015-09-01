#!/usr/bin/python
from fun_plots import *
from visual import*
from visual.graph import*
def plot_graph(f,value_format):
	gd = gdisplay(x=0, y=0, width=750, height=750,
      		title='Graph of functions in fun_plots', xtitle='x', ytitle='y',
      		foreground=color.white, background=color.black,
      		xmax=10, xmin=-10, ymax=10, ymin=-10)
	f1=gcurve(color=color.red)
	for x in value_format:
		f1.plot(pos=(x,f(x)))
	g1=gcurve(color=color.green)
	h=10e-10
	for x in value_format:
		g1.plot(pos=(x,float(f(x+h)-f(x))/h))
	#I choosed that integrale always passed in (-1,0)
	h1 = gcurve (color = color.yellow)
	t = -1
	y = 0
	h = (20 - 0) / float (1000)
	temps = [-10]
	fonction = [0]
	for i in range (1000):
		y += h * f (t)
		t += h
		h1.plot(pos=(t,y))

