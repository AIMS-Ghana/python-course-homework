#!/usr/bin/python3
import sys
import math

def random_pi_circ(seed,N):

 import sys
 import random as ran  
 from math import sqrt  
 
 
 Nint = int(float(N)/2.0)   # otherwise range complains division by 2 removes bias
 
 print(Nint)

 # now we go Monte-Carlo'ng

 inside=0   

 ran.seed(seed) 
 
 for i in range(0,Nint):  
    x=ran.random()  
    y=ran.random()  
    if x*x+y*y <1:  
        inside+=1  
    pi=4.0*inside/float(Nint)  # 4 from octants
 
 return pi 


def random_pi_sphere(seed,N):

 import sys
 import random as ran  
 from math import sqrt  
 

 Nint = int(float(N)/3.0)  # otherwise range complains, 3 takes care of bias
 
 print(Nint)

 # now we go Monte-Carlo'ng

 inside=0  

 ran.seed(seed) 
 
 for i in range(0,Nint):  
    x=ran.random()  
    y=ran.random()
    z=ran.random()  
    if x*x+y*y+z*z <1:  
        inside+=1  
    pi=6.0*inside/float(Nint)  # 6 is 8 (from 3d octants) x (3/4) from sphere to cube ratio....
 
 return pi 



if __name__ == "__main__":  

  print("circle-area pi:",random_pi_circ(sys.argv[1],sys.argv[2]))

  print("sphere-volume pi:",random_pi_sphere(sys.argv[1],sys.argv[2]))
 
