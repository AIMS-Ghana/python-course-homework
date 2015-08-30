import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import *
import fun_plots

t1 = np.arange(0.0, 20.0, 0.1)


def derivative(f,x, h=0.0001):
    deriv = (f(x+h)- f(x-h))/(2*h) 
    return deriv


#print (y)
def plotting(f):
		plt.figure(1)
		
		ax = plt.gca()
		ax.set_axis_bgcolor('black')
		#y=cumtrapz(t1, initial=0)\
		def Int(I,x):
			return f(x)
		y=odeint(Int,.01,t1)

		#y=quad(f,t1[0],t1[-1])
		#y=quad(f, rangex[0], rangex[-1])
		print (y)
		plt.plot(t1,derivative(f,t1), 'y',label='derivative')
		plt.plot(t1, f(t1), 'b',label='Original')
		plt.plot(t1,y,  'r',label='Integral')
		plt.title("Function, its derivative and integral ")
		plt.legend(loc='upper left')

		plt.show()




