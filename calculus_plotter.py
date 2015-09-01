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
      
      name = f.__name__  # gets the name of a function

      def h(I,x):       # this works if I don't use a lambda function, I is throwaway
       return f(x)      # gets rid of the missing argument problem

      plt.plot(x,f(x),label=name)
      plt.plot(x1,np.diff(f(x))/np.diff(x),color='red',label = "d/dx("+name+")")
 #     plt.plot(x,odeint(lambda I,x:f(x),fa,x),color='green', label = "int("+name+")") #notice the lambda function to insure there are TWO arguments for the rhs on odeint 
      plt.plot(x,odeint(h,fa,x),color='green', label = "int("+name+")") # this works too with previously defined h
      plt.xlabel('x',style='italic')
      plt.ylabel("f(x), f'(x) and int f(x)",style = 'italic')
      plt.legend(loc='best')
     
      plt.show()
     

      

      # unused output to pdf
      #plt.savefig("function_plots.pdf")
      



if __name__ == "__main__":

   
   
   funcplot(np.cos,[0.01,2*math.pi,100])

   
