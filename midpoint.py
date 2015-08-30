#!/usr/bin/python

def integMid(a,b,f,nbins=10):
       h=float(b-a)/nbins
       assert h>o
       assert type(nbins)==int
       sum=0.0
       x=a+h/2
while(x<b):
     sum+=h*f(x)
     x+=h
 return sum
