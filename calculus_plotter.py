#!/usr/bin/env python3
import scipy
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.integrate import quad



from scipy.integrate import quad

def Function(f, t):
	ans= quad(f(t), t)
	return ans
 

def Function2(f,t):
	scipy.misc.derivative(f, t, dt=1*e**(-6), n=1, args=(), order=1)


# evenly sampled time at 200ms intervals
t = np.arange(0., 50., 0.2)

# red dashes, blue squares and green triangles


if __name__=="__main__":

	a=sys.argv[0]
	
	plt.plot(t, a, 'r--', t,  Function2(a)   , 'bs', t,   Function(a), 'g^')
	plt.title('Graphs for the exp_saturation with its derivative and integral')
	plt.show()

