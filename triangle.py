#!/usr/bin/python

import sys 
a=float(sys.argv[1]) 
b=float(sys.argv[2]) 
c=float(sys.argv[3]) 

while a<=0 or b<=0 or c<=0: 
  print("enter only positive number ") 

if a>= b+c or b>=a+c or c>=a+b: 
  print ("wrong triangle ") 
else : 
 p= a+b+c 
 d=p/2 
 from math import sqrt 
 s=sqrt(d*(d-a)*(d-b)*(d-c)) 
 print (p,s) 


