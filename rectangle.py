#! /usr/bin/python
import sys

def check (a,b):
    assert (a>0) & (b>0) 

    s=a+b
    d=a-b
    assert (s>b) & (d<b), "violated rectangle inequality"

def perimeter(a,b):
    check(a,b)
    return a+b
    

def area(a,b):
    check(a,b)
   
    u=2*(l+b)
    s= (l+b)
    res= u 
         
    return res

 
if__name__=="__main__":
   a=float(sys.argv[1])
   b=float(sys.argv[2])
print("area {}, perimeter {}" .format(area(a,b) , perimeter(a,b)))


