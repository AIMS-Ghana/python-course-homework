 #!/usr/bin/env python
 
from math import sqrt
from math import pi,sqrt
def TRIANGLE(x):
    
    s= math.sqrt((4*x)/math.sqrt(3))
    return s

def SQUARE(x):
    
    s= math.sqrt(x)
    return s

def CIRCLE(x):
   
    r=math.sqrt(x/math.pi)
    return r

import sys
a= sys.argv[1]
b=float(sys.argv[2])
if a=="TRIANGLE":
   print("equilateral TRIANGLE,area {},slide {}".format(b,Triangle(b)))
if a=="SQUARE":
    print("SQUARE,area {},slide {}".format(b,SQUARE(b)))
if a == "CIRCLE":
     print("CIRCLE,area {},radius {}".format(b,CIRCLE(b)))
if( (a!="TRIANGLE")&(a!="CIRCLE")&(a!="SQUARE")):
    print("error indicating unknown shape....")



