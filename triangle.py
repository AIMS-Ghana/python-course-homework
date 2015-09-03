#!/usr/bin/python3


def perimeter(a,b,c):
    check(a,b,c)
    return a + b + c


def area(a,b,c):
    check(a,b,c)
    s = perimeter(a,b,c)/2.
    return (s*(s-a)*(s-b)*(s-c))**0.5


def check(a,b,c):
    assert (a > 0) & (b > 0) & (c >0), "I'm afraid side lengths can only be positive."
    assert (a + b > c) & (a + c > b) & (b + c > a), "Maybe you have got some funky geometry going on there; that is not a triangle."
    pass

if __name__ == "__main__":
    import sys
    assert (len(sys.argv) == 4), "I need exactly 3 sides, please."
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    print("area {}".format(area(a,b,c)))
    print("perimter {}".format(perimeter(a,b,c)))
