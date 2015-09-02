#!/usr/bin/python

def root(f,rangex,error_tolerance=1.0e-10,steps=100):
    ss = 0
    for i in range(len(rangex)-1):
        a = rangex[i]
        b = rangex[i-1]
        d = b-a
        e = f(b) - f(a)
        ss = a-d*f(a)/e 
        fs = f(ss)
        if (fs <= error_tolerance) or (steps == 0):
            return ss
        else:
            return root(f, rangex, error_tolerance, steps)
    
        
    
