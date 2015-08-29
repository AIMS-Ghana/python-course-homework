#!/usr/bin/python3

def check(i, j, k):
    s = i + j
    d = i - j
    assert (i > 0) & (j > 0) & (k > 0), "you entered a negative number"
    assert (s > k) & (d < k), "you entered an invalid number"
    pass


def perimeter(i, j, k):
    check(i, j, k)
    return (i+j+k)


def area(i, j, k):
    check(i, j, k)
    s1 = (i + j + k) / 2
    A = (s1 * (s1 - i) * (s1 - j) * (s1 - k)) ** 0.5
    return A


import sys

if __name__ == "__main__":
    i = float(sys.argv[1])
    j = float(sys.argv[2])
    k = float(sys.argv[3])
    # perimeter = float(sys.argv[1])+float(sys.argv[2])+float(sys.argv[3])

    #perimeter = i + j + k
    # s=perimeter/2
    # area=(s*(s-i)*(s-j)*(s-k))*0.5
    print("the area is:", area(i,j,k))
    print("the perimeter is:", perimeter(i,j,k))
