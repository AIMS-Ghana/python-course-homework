#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from  sympy import *
from scipy.misc import derivative as deriv
from scipy.integrate import odeint
import math

'''
def somefunction(f,xs):

    ys = f(xs)  # real version from function
    Iys = xs**2/2     # someintegralfunc(f, xs) real version from some integrator
    plt.figure(1)
    plt.plot(xs,ys)
    plt.plot(xs,Iys)
    plt.show()

def somef1(xs):
    return xs

xs = np.arange(0.0, 5.0, 0.1)
somefunction(somef1,xs)

'''
def somefunction(f, xs):
    ys = f(xs) # real version from function
    yprimes = deriv(f,xs) #np.exp(-xs) # somederivfunc(f, xs) real version from some derivative finder
    Iys =  odeint(lambda I,x:f(x),0,xs) # xs + np.exp(-xs) # someintegralfunc(f, xs) real version from some integrator
    plt.figure(2)
    plt.plot(xs,ys)
    plt.plot(xs,yprimes)  #differention
    plt.plot(xs,Iys)  #integration
    plt.show()

def somef(xs):
    return 1-np.exp(-xs)

xs = np.arange(0.0, 5.0, 0.1)

somefunction(somef, xs)
'''
def something3(f, xs):
    ys = f(xs) # real version from function
    yprimes = 5*ys # somederivfunc(f, xs) real version from some derivative finder
    Iys = np.exp(5*xs)/5 # someintegralfunc(f, xs) real version from some integrator
    plt.figure(3)
    plt.plot(xs,ys)
    plt.plot(xs,yprimes)  #differention
    plt.plot(xs,Iys)  #integration
    plt.show()

def somef3(xs):
    return np.exp(5*xs)

x1 = np.arange(0.0, 5.0, 0.1)

something3(somef3, x1)

def something4(f, t):
    ys = f(t) # real version from function
    yprimes = np.cos(t)-np.sin(t) # somederivfunc(f, xs) real version from some derivative finder
    Iys = np.sin(t) - np.cos(t) # someintegralfunc(f, xs) real version from some integrator
    plt.figure(4)
    plt.plot(t,ys)
    plt.plot(t,yprimes)  #differention
    plt.plot(t,Iys)  #integration
    plt.show()

def somef4(t):
    return np.sin(t) + np.cos(t)

t = np.arange(0.0, 5.0, 0.1)

something4(somef, t)


def something5(f, t):
    ys = f(t) # real version from function
    yprimes = (-2*t) * np.cos(t**2) # somederivfunc(f, xs) real version from some derivative finder
    Iys = (t/2 + (1/4) * np.cos(2*t)) # someintegralfunc(f, xs) real version from some integrator
    plt.figure(5)
    plt.plot(t,ys)
    plt.plot(t,yprimes)  #differention
    plt.plot(t,Iys)  #integration
    plt.show()

def somef5(t):
    return np.sin(t)**2

t = np.arange(0.0, 5.0, 0.1)

something5(somef5, t)
'''