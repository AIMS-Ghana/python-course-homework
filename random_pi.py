#!/usr/bin/python3
import sys
import math

def random_pi_circ(seed,N):

 import sys
 import random as ran  
 from math import sqrt  
 
 
 N = int(sys.argv[2])
 
 
 

 inside=0 

 ran.seed(seed) 
 
 for i in range(0,N):  
    x=ran.random()  
    y=ran.random()  
    if sqrt(x*x+y*y)<=1:  
        inside+=1  
 pi=4.0*inside/N
 
 return pi 


def random_pi_sphere(seed,N):

 import sys
 import random as ran  
 from math import sqrt  
 

 N = int(sys.argv[2])
 
 

 inside=0  

 ran.seed(seed) 
 
 for i in range(0,N):  
    x=ran.random()  
    y=ran.random()
    z=ran.random()  
    if sqrt(x*x+y*y+z*z)<=1:  
        inside+=1  
 pi=6.0*inside/N
 
 return pi 



if __name__ == "__main__":  

  print("circle-area pi:",random_pi_circ(sys.argv[1],sys.argv[2]))

  print("sphere-volume pi:",random_pi_sphere(sys.argv[1],sys.argv[2]))
 
