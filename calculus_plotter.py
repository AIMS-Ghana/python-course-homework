#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

from scipy.misc import derivative
from scipy.integrate import odeint




def plotter(f): ###function of f with 'rag'(range) as values
		def g(Int_f,rag):
		 	return f(rag)
		plt.figure()
		rag=np.arange(0,50,.01) 
		plt.plot(rag,f(rag),'r',label='function',lw=2)
		plt.ylabel('Y')
		plt.xlabel('X')
		Der_f = derivative(f,rag,dx=1,n=1) #differentiating a function "f"
		Int_f = odeint(g, 0,rag) #integrating a function "f"
		plt.plot(rag,Der_f,'g',label='derivative',lw =2)	
		plt.plot(rag,Int_f,'bo',label='integrate',lw =2)	
		plt.legend()
		plt.show()



