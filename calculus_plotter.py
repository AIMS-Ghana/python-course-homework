#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative as deriv
import scipy.integrate as integ

f = lambda x: x

x = np.linspace(-np.pi,np.pi,256,endpoint = True) # range of x values on graph
y,dydx = x,deriv(f,x)  # define the y values on graph
plt.plot(x,y,'r') # plot x against y
plt.plot(x,dydx,'g')
plt.xlabel('x-axis') # label x-axis
plt.ylabel('y-axis') # label y-axis
plt.show() # show graph

f = lambda x: 1 - np.exp(-x)

x = np.linspace(-np.pi,np.pi,256,endpoint = True) # range of x values on graph
y,dydx = 1 - np.exp(-x),deriv(f,x)  # define the y values on graph
plt.plot(x,y,'r') # plot x against y
plt.plot(x,dydx,'g')
plt.xlabel('x-axis') # label x-axis
plt.ylabel('y-axis') # label y-axis
plt.show() # show graph

f = lambda x: np.exp(5*x)

x = np.linspace(-np.pi,np.pi,256,endpoint = True) # range of x values on graph
y,dydx = np.exp(5*x),deriv(f,x)  # define the y values on graph
plt.plot(x,y,'r') # plot x against y
plt.plot(x,dydx,'g')
plt.xlabel('x-axis') # label x-axis
plt.ylabel('y-axis') # label y-axis
plt.show() # show graph

f = lambda t: np.sin(t) + np.cos(t)

t = np.linspace(-np.pi,np.pi,256,endpoint = True) # range of x values on graph
y,dydx = np.sin(t) + np.cos(t),deriv(f,t)  # define the y values on graph
plt.plot(t,y,'r') # plot x against y
plt.plot(t,dydx,'g')
plt.xlabel('x-axis') # label x-axis
plt.ylabel('y-axis') # label y-axis
plt.show() # show grap

f = lambda t: np.sin(t)**2

t = np.linspace(-np.pi,np.pi,256,endpoint = True) # range of x values on graph
y,dydx = np.sin(t)**2,deriv(f,t)  # define the y values on graph
plt.plot(t,y,'r') # plot x against y
plt.plot(t,dydx,'g')
plt.xlabel('x-axis') # label x-axis
plt.ylabel('y-axis') # label y-axis
plt.show() # show grap

