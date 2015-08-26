#!/usr/bin/python


def check(i, j):
    s = i + j
    d = i - j
    assert (i > 0) & (j > 0),"you entered a negative number"
    assert (s > i) & (d < j), "you entered an invalid number"
    pass


def perimeter(i, j):
    check(i, j)
    p= (2*i)+(2*j)
    return p


def area(i, j):
    check(i, j)
    A = (i * j)
    return A


import sys

if __name__ == "__main__":
    i = float(sys.argv[1])
    j = float(sys.argv[2])
    #  k = float(sys.argv[3])
    # perimeter = float(sys.argv[1])+float(sys.argv[2])+float(sys.argv[3])

    #perimeter = (2 * i) + (2 * j)
    # s=perimeter/2
    # area=(s*(s-i)*(s-j)*(s-k))*0.5
    print("the area is:", area(i, j))
    print("the perimeter is:", perimeter(i, j))
