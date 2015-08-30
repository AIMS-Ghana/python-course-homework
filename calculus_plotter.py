#!/usr/bin/env python3
import scipy
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.integrate import odeint




def Function(f, t):
	ans= odeint( lambda t:f(t), t , tol=1*e**(-5))
	return ans
 

def Function2(f,t):
	scipy.misc.derivative(f, t, dt=1*e**(-6), n=1, args=(), order=1)


# evenly sampled time at 200ms intervals
t = np.arange(0., 50., 0.2)

# red dashes, blue squares and green triangles


if __name__=="__main__":

	a=sys.argv[0]
	
	plt.plot(t, a, 'r--', t,  Function2(a)   , 'bs', t,   Function(a), 'g^')
	plt.title('Graphs for the {} with its derivative and integral').format(a)
	Red_dashes = mlines.Line2D([], [], color='red', marker='--', markersize=15, label='red dashes')
	Blue_squares = mlines.Line2D([], [], color='blue', marker='square',markersize=15, label='blue squares')
	Green_triangles = mlines.Line2D([], [], color='green', marker='triangle',markersize=15, label='green triangles')
	plt.legend(handle1 = Red_dashes , handle2 = Blue_squares , handle3 = Green_triangles )
	plt.show()

