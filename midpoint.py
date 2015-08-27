#!/usr/bin/python3
import sys
import math
import numpy as np


def integrate(f, *args):
   # stuff is inputting [a,b] only 
   # nbins=100
    
    N = len(args[0])

   # assert N == 2, "Start and end only, pal"
    

   # a = args[0][0]
   # b = args[0][1]
   # h = float(b - a)/float(nbins)

    xi = args[0]
    mid = []
    hi = []
    
    
    for i in range(0,N-1):
      mid.append(f((xi[i]+xi[i+1])/2.0))
      hi.append((xi[i+1]-xi[i]))
    
    
    
    ans = sum([mid[i]*hi[i] for i in range(len(mid))])
      
    
    
    #ans = 0.0
    #x = a + h/2                 
    #while (x < b):
    #    ans += h * f(x)
    #    x += h

    return ans

if __name__ == "__main__":

    def func(x):
     return x - x**2
#   xrange = [0,1]
    xrange = np.linspace(0,1,100)
 
    print(integrate(func,xrange))
    
