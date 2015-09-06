#!/usr/bin/python


from numpy import *

from scipy.integrate import odeint
def calc_all(f, rangex, ifmin=0):
     fx=f(rangex)
     return {
         'f' : fx,
         'df' : gradient(fx),
          
         'If' : odeint(lambda y, x:f(x),0,rangex)
    }
import matplotlib.pyplot as plt
def f(x):
	x**(2)
def plot_all(f, rangex, ifmin=0):
    lines=calc_all(f, rangex, ifmin)
    fx, =plt.plot(rangex, lines['f'],'--')
    df, =plt.plot(rangex, lines['df'],".")
    If, =plt.plot(rangex, lines['If'],"-") 
    plt.legend([fx, df, If],
['function', 'derivative', 'integral'])
    plt.show()

if __name__ == " __main__":
   from numpy import linspace
   x=arange(0,10,0.01)
   
   
   plot_all(lambda x:x,x)




import sys
import pylab
import numpy
import fun_plots as fp
from scipy.misc import derivative

x = numpy.arange(0,10,0.01) # 100 linearly spaced numbers
# compose plot

def plotter(f):
	pylab.figure()
	df = derivative(f,x,dx=1,n=1)
	
	pylab.plot(x,f(x), 'b', label = "f(x)")
	pylab.plot(x,df,'r', label = "f'(x)")
	pylab.legend()
	pylab.show() # show the plot

plotter(numpy.cos)

