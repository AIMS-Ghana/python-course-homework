#!/usr/bin/env python

import random  
import sys
from numpy import sqrt
#calculating Pi using Monte Carlo Method

seed=int(sys.argv[1]) 
n=int(sys.argv[2])  
count_inside=0
random.seed(seed)

#def pi_circlearea():
for i in range(n):  
	x=random.random()  
	y=random.random()
	
        if sqrt(x*x+y*y)<=1:              
		count_inside+=1
	else:
		pass 
	pi_circlemethod=4.0*count_inside/n  
print "The circle-area method pi:" , pi_circlemethod

#def p_spherevolume():

# using sphere-volume method to find pi
c_inside=0
for i in range(n):  
	x=random.random()  
	y=random.random()
	z=random.random()
	
        if sqrt(x*x+y*y+z*z)<=1:              
		c_inside+=1
	else:
		pass 
	pi_spheremethod=6.0*c_inside/n 

print "The sphere-volume method pi:" , pi_spheremethod

'''
pi_value_sphere = (6)*(float(num_of_pts_in_sphere)/float(num_of_pts))
	pi_values = [pi_value_circle,pi_value_sphere]	
	return pi_values

if __name__ == "__main__":
	if len(sys.argv) ==3:
              
              random.seed(int(sys.argv[1]))
              h,k = gen(int(sys.argv[1]),int(sys.argv[2]))
	      print 'circle-area pi:',h,'\nsphere-volume pi:',k



 '''
