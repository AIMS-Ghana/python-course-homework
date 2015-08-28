#!/usr/bin/python3
import sys
import math


def root(f, *args):
    
    n = 1
    NMAX = 1000
    tol = 0.0001

    a=float(args[0][0])
    
    b=float(args[0][1])
    

    while n <= NMAX: 
        c = (a + b)/2 
        if f(c) == 0 or abs((b - a)/2) < tol:
            print(c)
            sys.exit(0)

        n = n + 1 
        if f(c)*f(a) >0:
            a = c
        else:
            b = c 
    
   




if __name__ == "__main__":

   
    def func(x):
     return x - x**2
       
    
    x = root(func, [0.5,1.5])
   

