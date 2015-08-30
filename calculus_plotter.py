#!/usr/bin/python
 
from visual.graph import * # import graphing features


def approprim (a, b, x, g): # g is a function
	A = float (g (b) - g (a)) / (b - a)
	B = g (b) - (A * b)
	return ((float (A) / 2) * (x ** 2)) + (B * x)

def draw_curve (F, V):	
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

	f3 = gcurve (color = color.yellow) # the integral function graphics curve
	for x in V :
		y = approprim (x, x + 0.1, x, F)
		f3.plot (pos = (x, y))


	




