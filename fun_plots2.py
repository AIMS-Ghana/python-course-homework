
import numpy as np

def form(x):
	return x

def diff(x):
	return np.exp(-x/2)

def play(x):
	return np.sin(x)*tan(x)

def tan(x):
	return np.tan(x**2)

def value(x):
	return 3 - np.sin(x)**2

funclist = [
	form, diff, play, tan, value
]
