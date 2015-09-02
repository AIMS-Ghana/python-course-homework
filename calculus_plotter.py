#!/usr/bin/python
 
from visual.graph import * # import graphing features
from scipy.integrate import *


def draw_curve (F, V):

	def func(m, x):
		return F (x)
	
	gd = gdisplay(x = 0, y = 0, width = 1500, height = 1500, # control the window
		title = 'Graph', xtitle = 'x', ytitle = 'y',
		foreground = color.white, background = color.black,
		xmax = 20, xmin = -20, ymax = 50, ymin = -50)
	label (display = gd.display, pos=(-17.5, 50), text="_____ function \n_____ derivate function \n_____ integral function")

	f1 = gcurve(color = color.red) # the function graphics curve
	for x in V :
		f1.plot(pos = (x, F (x))) # plot

	f2 = gcurve (color = color.green) # the derivative function graphics curve
	for x in V :
		h = 0.00000000001
		y = float (F (x + h) - F (x - h)) / (2 * h)
		f2.plot (pos = (x, y))

	h1 = gcurve (color = color.yellow)
    	t = 0
    	y = 0
    	h = 20 / 1000.0
    	temps = [0]
    	fonction = [0]
    	for i in range (1000):
        	y += h * F (t)
        	t += h
        	h1.plot(pos=(t,y))


	




