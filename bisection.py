#!/usr/bin/python
def root (function,lower_bound,upper_bound,error_tolerance=1.0e-10):
    fu=function(upper_bound)
    if fu==0.0 :  return upper_bound
    fl=function(lower_bound)
    if fl==0.0 :  return lower_bound
    if fu*fl > 0.0:  
        return None
    else:
        mid=(lower_bound+upper_bound)/2
        error=(upper_bound-lower_bound)/2
        while(error>error_tolerance): 
            fu=function(upper_bound)
            fl=function(lower_bound)

            if mid==0.0 : return mid

            elif fu*mid < 0.0 : lower_bound=mid

            elif fl*mid < 0.0 : upper_bound=mid
            
            mid=(lower_bound+upper_bound)/2
            error=(upper_bound-lower_bound)/2
        return mid

def func(x):  
    return x**3-3*x+1     
   
    x=bisection(func,1.0,2.0,error_tolerance=1.0e-10)
    print x

