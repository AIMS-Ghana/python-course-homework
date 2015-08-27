#!/usr/bin/python

def integrate(f, y):
# calculating the mid point, function to find integrator

      for n in range (len(y-1)):
          w= 0.00
          interval= y[n]-y[n-1]
          height = f(y[n]+y[n-1]/2)
          midpt=float (y[n]+y[n-1]/2)
      
          w= midpt+interval*height

      return w  

    

    



