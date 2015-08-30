#!/usr/bin/env python

#function that plots a function, it's derivative and integral
from pylab import *
from scipy.misc import derivative
from scipy.integrate import odeint
import fun_plots

plotlist= [r'$f(x) = x$' , r'$f(x) = 1-e^{-x}$',r'$f(x) = e^{5x}$',r'$f(x) = \sin(t) + \cos(t)$',r'$f(x) = \sin^{2}(t)$']

def fplot(fxn,i):
    figure(i+1),grid(True)
    title("A graph for {0} it's derivative and integral".format(plotlist[i]))
    xlabel("X axis")
    ylabel("Y axis")
    xticks(arange(0,10,1))

    X = arange(0,10,0.01)

    def func(I,X):
	return fxn(X)
    Ifxn = odeint(func,0,X)
    Dfxn = derivative(fxn,X,dx=1,n=1)

    plot(X,fxn(X), 'b', lw = 2, label = r'$f(x)$')
    plot(X,Dfxn, 'm', lw = 2, label = r'$f\prime(x)$')
    plot(X,Ifxn, 'g', lw = 2, label = r'$\int{f(x)}dx$')
    legend()
    show()
	

