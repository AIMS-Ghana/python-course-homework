
from pylab import *
from scipy.misc import derivative
from scipy.integrate import odeint

#import fun_plots as fp
#from simpy import integrate

funames = [r'$f(x) = x$' , r'$f(x) = 1-e^{-x}$',r'$f(x) = e^{5x}$',r'$f(x) = \sin(t) + \cos(t)$',r'$f(x) = \sin^{2}(t)$']

def plotter(fxn,i):
    figure(i+1),grid(True)
    title(" A graph of {0} with it's derivative and integral".format(funames[i]))
    xlabel("X")
    ylabel(r'\f(x) , \f\prime(x) , \$\int{f(x)}$')
    xticks(arange(0,10,1))

    X = arange(0,10,0.01)

    def k(I,X):
	return fxn(X)

    Dfxn = derivative(fxn,X,dx=1,n=1)
    Ifxn = odeint(k,0,X)

    plot(X,fxn(X), 'r', lw = 2, ms = 3, label = "f(x)")
    plot(X,Dfxn, 'b', lw = 2, ms = 3, label = "f'(x)")
    plot(X,Ifxn, 'g', lw = 2, ms = 3, label = r'$\int{f(x)}$')
    legend()
    show()
