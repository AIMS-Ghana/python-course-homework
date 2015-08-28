#!/usr/local/bin/python3

def check(L,l):
    assert (L>0) & (l>0),"entered negative dimension"

def area(L,l):
    check(L,l)
    A=L*l
    return A
def perimeter(L,l)
    check(L,l)
    p=(L+l)*2
    return p

import sys
if __name__=="__main__":
L=float(sys.argv[1])
l=float(sys.argv[2])
print("The area is {},  The perimeter is {}".format(area(L,l),perimeter(L,l)))

