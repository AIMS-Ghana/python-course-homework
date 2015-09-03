#!/usr/bin/python

import math

def root(f,interval, tol=1e-5, steps=100):
	p_0 = interval[0]
	p_1 = interval[-1]
        i = 2
        while i < steps:
	
                q_0 = f(p_0)
		q_1 = f(p_1)
		
		
                p = 0.0
		p = p_1 - q_1*(p_1-p_0)/q_1-q_0
	
		if abs(p - p_1) < tol:
			return p
                
	        else:
			p_0 = p_1
			q_0 = q_1
			p_1 = p
			q_1 = f(p)
	
                  
		
		
	


