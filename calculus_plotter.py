#!/usr/bin/python

from scipy.misc import derivative as deriv
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10., 0.1)
f = np.sin(x)/x

d = deriv(f,x)

plt.plot(x,f(x), marker='*', linestyle='-', color='y', label='f(x)')
plt.plot(x,d, marker='o', linestyle='.', color='r', label='d(f(x))')
plt.xlabel('x Values')
plt.ylabel('function/Derivative')
plt.title('Plots of a function and its Derivative')
plt.show()
