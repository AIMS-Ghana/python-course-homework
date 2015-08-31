#!/usr/bin/python
import math 

def perimeter(a): 
    check(a) 
    p = math.pi*(a)**2 
    return p 

def area(a): 
    check(a) 
    p=perimeter (a) 
    res=math.pi*(a)**2 
    return res
 
def check(a): 
    assert (a>0), "negative dimension" 
    

import sys 
if __name__ == "__main__": 

    a = float(sys.argv[1]) 
    print "area{},\n perimeter{}".format(area(a), perimeter(a))
