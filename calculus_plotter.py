#!/usr/bin/env python3
import scipy
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.integrate import odeint
from scipy.misc import *
from scipy.integrate import odeint




def plotting (f,x):
	def h(I,x):
		return f(x)

	I = odeint(h , 0 , x)
	return I

x=np.arange(0,10.0,0.1)

f= x**2
plt.plot(x, f)
