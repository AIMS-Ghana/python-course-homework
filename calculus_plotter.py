#!/usr/bin/python3
import sys
import math
import numpy as np
import scipy as sp


def funcplot(f, *args):
      
 

      import sys
      import math
      
      
      import matplotlib.pyplot as plt
      import numpy as np
      import scipy as sp
      from scipy.integrate import odeint

     
      
      Nargs = len(args)     # read in arguments
      a = args[0][0]
      b = args[0][1]
      N = args[0][2]
 
      h = float((a + b)/N)     # offsets for df(x) plot
      a1 = a+h
      b1=  b-h

      fa = f(a)
    

      x = np.linspace(a,b,N)        # N points for f(x)

      x1 = np.linspace(a1,b1,N-1)   # since np.diff puts values at N-1 midpoints             
      
     

      fig1 = plt.figure()
      ax1 = fig1.add_subplot(3,1,1)
      ax2 = fig1.add_subplot(3,1,2)
      ax3 = fig1.add_subplot(3,1,3)
      
    
      
      ax1.plot(x,f(x))
      ax2.plot(x1,np.diff(f(x))/np.diff(x))
      ax3.plot(x,odeint(lambda y,x:f(x),fa,x))

      

      plt.show()
      #plt.savefig("function_plots.pdf")
      



if __name__ == "__main__":

   
   
   funcplot(np.cos,[0.01,2*math.pi,100])

   
