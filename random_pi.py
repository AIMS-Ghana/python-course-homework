#!/usr/bin/python
#calculation of pi using the mornte carlo method
import random 
import math 
import sys
inside=0  
seed=int(sys.argv[1])
n=int(sys.argv[2])
random.seed(seed)  
for i in range(n):  
    x=random.random()  
    y=random.random() 
    z=random.random() 
    if math.sqrt(x*x+y*y)<=1:  
        inside+=1  
circle_pi=4.0*inside/n  
count = 0
for i in range(n):
	x=random.random()  
        y=random.random() 
        z=random.random()
        distance = math.sqrt(x * x + y * y + z * z)
	if distance <= 1:
		count += 1
	else:
		pass

sphere_pi = 6.0*count/n
print "circle pi:", circle_pi , "sphere pi:", sphere_pi




