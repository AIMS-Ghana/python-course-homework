#!/usr/bin/python


from scipy.misc import derivative
from scipy.integrate import odeint
import matplotlib.pylab as plt
import numpy as np

def fn_plotter(f_n):
    def m(I,x):
        return f_n(x)
    plt.figure()
    x = np.arange(0.0, 20.0, 0.01)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')

    Df_n = derivative(f_n, x, dx=1, n=1)
    If_n = odeint(m, 0, x)
    plt.plot(x,f_n(x), 'g', lw= 3, label= 'My function' )
    plt.plot(x,Df_n, 'r', lw =2, label='Derivative')
    plt.plot(x,If_n, 'bo',lw=3, label='Integral')

    plt.legend()
    plt.show()


