#!/usr/bin/python
#calculation of pi using the mornte carlo method
from numpy.random import uniform , seed

def get_samples(how_many,dim):
    return uniform(size=(how_many/dim,dim))


def is_in_circ(x,y):
    return (x**2+y**2)<1

def is_in_sph(x,y,z):
    return (x**2+y**2+z**2)<1


def est_pi_circ(in_circ,tot):
    return (4.0*in_circ)/tot


def est_pi_sph(in_sph,tot):
    return (6.0*in_sph)/tot



if __name__ =="__main__":

        import sys
        seed=(int(sys.argv[1]))
        samples=int(sys.argv[2])
	circ_samples=get_samples(samples,2)
	in_circ=sum(is_in_circ(circ_samples[:,0],circ_samples[:,1]))
	vol_samples=get_samples(samples,3)
	in_sph=sum(is_in_sph(vol_samples[:,0],vol_samples[:,1],vol_samples[:,2]))


#print (est_pi_circ,samples/2)
#print (est_pi_sph,samples/3)
print in_circ
print in_sph



'''
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
'''



