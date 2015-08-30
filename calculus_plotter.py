#!/usr/bin/python
from scipy.misc import derivative as deriv
import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt

f = lambda x : 1 / (1 + x**2)

x = np.arange(-10, 10, 0.01)

d = deriv(f,x)

i = [integ.quad(f,-np.inf,tau)[0]for tau in x]

plt.plot(x,f(x),'r-')
plt.plot(x,d,'b-')
plt.plot(x,i,'g-')
plt.ylim(-1.5,1.5)
plt.show()
