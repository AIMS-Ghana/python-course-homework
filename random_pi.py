#!/usr/bin/env python
import random
import sys
from numpy.random import seed
import numpy as np
'''
1. pick point at random in square(x,y)
2. set count to 0
3. check if point lies in circle: x^2 + y^2 < R^2 
4. if point in circle increment count
'''

def gen(seed, sample_size):
        num_of_pts_in_circle = 0
        num_of_pts_in_sphere = 0
        for num_of_pts in range(seed,sample_size):
		rand_x = random.random()
		rand_y = random.random()
                rand_z = random.random()#for the sphere
                #check if x^2 + y^2 < R^2 = 1
                if (rand_x*rand_x + rand_y*rand_y) < 1:
        		num_of_pts_in_circle += 1
                if (rand_x*rand_x + rand_y*rand_y + rand_z*rand_z) < 1:#do same for the sphere
			num_of_pts_in_sphere += 1       
		num_of_pts +=1
        #calculate pi using circle = 4 *(num_of_pts_in_circle/num_of_pts)
	pi_value_circle = 4*float(num_of_pts_in_circle)/float(num_of_pts)
	#calculate pi using sphere= 6 *(num_of_pts_in_sphere/num_of_pts)
	pi_value_sphere = (6)*(float(num_of_pts_in_sphere)/float(num_of_pts))
	pi_values = [pi_value_circle,pi_value_sphere]	
	return pi_values

if __name__ == "__main__":
	if len(sys.argv) ==3:
              
              random.seed(int(sys.argv[1]))
              h,k = gen(int(sys.argv[1]),int(sys.argv[2]))
	      print 'circle-area pi:',h,'\nsphere-volume pi:',k
              
