#!/usr/bin/python3
import sys
import math

def random_pi(seed,throws):

 import sys
 import random as ran  
 from math import sqrt  
 
 seed=sys.argv[1]
 N = int(sys.argv[2])
 print(N)
 

 inside=0  
 
 for i in range(0,N):  
    x=ran.random()  
    y=ran.random()  
    if sqrt(x*x+y*y)<=1:  
        inside+=1  
 pi=4.0*inside/N 
 print(pi) 

if __name__ == "__main__": 

 random_pi(sys.argv[1],sys.argv[2])


 
