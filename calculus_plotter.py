#!/usr/bin/env python
from pylab import *
from scipy import misc
import scipy.integrate as integrate 
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
import matplotlib.pyplot as plt
import numpy as np

def plotter(fonction):
	ax = subplot(111)
	x = arange(-3.0, 3.0, 0.01)
	y = fonction(x)
	plot(x, y,'r-')
	yp = misc.derivative(fonction, x)
	plot(x, yp,'b-')
	def h(I,x):
		return fonction(x)
	zp=integrate.odeint(h,0,x)
	
	plot(x,zp,'green')
	grid(True)
	ax.spines['left'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['bottom'].set_position('zero')
	ax.spines['top'].set_color('none')

	text(-0.75, 6.0,    r'function', horizontalalignment='center',  fontsize=18,color='red')

	text(-1.0, -8.0,   r"deriv", horizontalalignment='center', 	     fontsize=18,color='blue')
	text(-2.0, -8.0,   r"Inte", horizontalalignment='center', 	     fontsize=18,color='green')
	show()
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
from pylab import *
import matplotlib.pyplot as plt
import numpy as np


ax = subplot(111)

def fonction(x):
    return 1 - np.exp(-x)

x = arange(-3.0, 3.0, 0.01)

y = fonction(x)



plot(x, y,'r-')

yp = misc.derivative(fonction, x)

plot(x, yp,'b-')


grid(True)




ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

text(-0.75, 6.0,
     r'function', horizontalalignment='center',
     fontsize=18,color='red')

text(-1.0, -8.0,
     r"deriv", horizontalalignment='center',
     fontsize=18,color='blue')

show()
print np.cos
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
