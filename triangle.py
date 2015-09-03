#!/usr/bin/python

'''def check(x,y,z):
 assert x>0 and y>0 and z>0,"Entered a negative dimension."
 m=x+y
 n=x-y
 assert(m>z) and (n<z),"Violated the Triangular inequality."

def area(x,y,z):
 check(x,y,z)
 s=(x+y+z)/2
 res=((s*(s-x)*(s-y)*(s-z))**0.5)
 return res

def perimeter(x,y,z):
 check(x,y,z)
 return x+y+z

import sys

if __name__=="__main__":

 x=float(sys.argv[1])
 y=float(sys.argv[2])
 z=float(sys.argv[3])

print("area {}".format(area(x,y,z)))
print("perimeter {}".format(perimeter(x,y,z)))


#print "area " " {}, perimeter" " {}".format(area(x,y,z),perimeter(x,y,z))'''

def checkdim(a,b,c):
    assert (a >= 0) & (b >= 0) & (c >= 0), "Passed negative dimensions"
    assert (a+b > c) & (a+c > b) & (b+c > a), "Passed non-triangle dimensions"
    pass


def area(a, b, c):
    checkdim(a,b,c)
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5
    pass


def perimeter(a, b, c):
    checkdim(a,b,c)
    return a+b+c


import sys

if __name__ == "__main__":
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    print("area {}".format(area(a,b,c)))
    print("perimeter {}".format(perimeter(a,b,c)))







