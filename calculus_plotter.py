#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy.integrate import odeint

def drawgraph(F):
     def h(I,x):
        return F(x)

     plt.figure()
     X = np.arange(0,10,0.001)

     plt.xlabel("x")
     plt.ylabel("y")

     DF = derivative(F,X,dx=1,n=1)
     IF = odeint(h, 0, X)

     plt.plot(X,F(X),'r',label='f(x)',lw = 2)
     plt.plot(X,DF,'g',label='derivative',lw =2)
     plt.plot(X,IF,'bo',label='integral',lw =0.5)
     
     plt.legend()
     plt.show()
