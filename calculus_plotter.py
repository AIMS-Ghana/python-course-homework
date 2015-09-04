# -*- coding: utf-8 -*
import matplotlib.pylab as plt
import numpy as np
from scipy.misc import derivative
from scipy.integrate import odeint
def plotter(f):
     def g(I,x):
        return f(x)

     plt.figure()
     X = np.arange(0,10,0.01)
     plt.xlabel("x-axis")
     plt.ylabel("x-axis")
     Dfxn = derivative(f,x,dx=1,n=1)
     Ifxn=odeint(g, 0, x)
     plt.plot(X,f(x),'g',label='fxn',lw =2)
     plt.plot(X,Df,'r',label='derivative',lw =2)
     plt.plot(X,If,'bo',label='integral',lw =2)
     
     plt.legend()
     plt.show()
