#!/usr/bin/env python
import random
import sys
'''
1. pick point at random in square(x,y)
2. set count to 0
3. check if point lies in circle: x^2 + y^2 < R^2 
4. if point in circle increment count
'''


def gen(seed, sample_size):
        num_of_pts_in_circle = 0
        for num_of_pts in range(seed,sample_size):
		rand_x = random.random()
		rand_y = random.random()
                #check if x^2 + y^2 < R^2 = 1
                
                if (rand_x*rand_x + rand_y*rand_y) < 1:
        		num_of_pts_in_circle += 1
                        
		num_of_pts +=1
        #calculate pi = 4 *(num_of_pts_in_circle/num_of_pts)
	pi_value = 4*float(num_of_pts_in_circle)/float(num_of_pts)
	return pi_value

if __name__ == "__main__":
	if len(sys.argv) ==3:
	      print 'circle-area pi: ',gen(int(sys.argv[1]),int(sys.argv[2]))
