#!/usr/bin/python



#bisection function
def root(f,rangex,tol=1.0e-5):
    fu=f(rangex[1])
    if fu==0.0 :  
	return rangex[1]
    fl=f(rangex[0])
    if fl==0.0 : 
	 return rangex[0]
    if fu*fl > 0.0:  
        return None
    else:
        mid=(rangex[0]+rangex[1])/2
        error=(rangex[1]-rangex[0])/2
	
        while(error>tol): 
            fu=f(rangex[1])
            fl=f(rangex[0])
            fm=f(mid)
	    a = rangex[0]
	    b = rangex[1]

            if fm==0.0 : 
		return mid
            elif fu*fm < 0.0 : 
		a=mid
            elif fl*fm < 0.0 :
		 b=mid
            
            mid=(a+b)/2
            error=(b-a)/2
        return mid



