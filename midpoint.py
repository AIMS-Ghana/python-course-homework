#!/usr/bin/env python3
import math
import sys
from scipy.integrate import quad




def f(x):
	return math.exp(x)
    
def Intmid(f,a,b,nbins):
	h=float(b-a)/nbins
	sum=0.0
	x=a+h/2	
	while (x<b):
		sum+=h*f(x)
		x += h		
	return (sum)
