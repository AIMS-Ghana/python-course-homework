#!/usr/bin/python

def check(r):
  #  s = i + j
   # d = i - j
    assert (r > 0),"you entered a negative number"
  #  assert (s > i) & (d < j), "you entered an invalid number"
    pass
pi=3.14

def perimeter(r):
    check(r)
    c= 2*pi*r
    return c


def area(r):
    check(r)
    A = (pi*r*r)
    return A



import sys

if __name__ == "__main__":
    r = float(sys.argv[1])
   # j = float(sys.argv[2])
    #  k = float(sys.argv[3])
    # perimeter = float(sys.argv[1])+float(sys.argv[2])+float(sys.argv[3])

    #perimeter = (2 * i) + (2 * j)
    # s=perimeter/2
    # area=(s*(s-i)*(s-j)*(s-k))*0.5
    print("the area is:", area(r))
    print("the perimeter is:", perimeter(r))
