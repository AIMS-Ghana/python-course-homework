#!/usr/bin/python3

#Calculate the area and perimter of a circle, given its radius. 

def perimeter(a,b):
    check(a,b)
    return 2*(a + b)

def area(a,b):
    check(a,b)
    return a*b

def check(a,b):
    assert (a > 0) & (b >0), "Rectangle can only have positive dimensions"
    pass

if __name__ == "__main__":
    import sys
    assert (len(sys.argv) == 2) or  (len(sys.argv)==3), "Number of arguments specified not appropiate."
    a = float(sys.argv[1])
    b = float(sys.argv[-1])
    print("area {}".format(area(a,b)))
    print("perimeter {}".format(perimeter(a,b)))
