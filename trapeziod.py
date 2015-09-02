#!/usr/bin/env python

#Intergrate using trapezoidal rule

#A=h/2(a+b)

def integrate_trap(f, a, b, n):    
    sum=0
    width= float(b-a)/n
    assert width > 0
    assert type(n) == int
    
    sum = (width/2) * (f(a) + f(b))
    for n in range(1, n):    
        sum += width * f(a + n*width)
    
    return sum


