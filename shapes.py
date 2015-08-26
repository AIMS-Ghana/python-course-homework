#!/usr/bin/python3

def circle(a):
    from math import pi
    check(a)
    return (a/pi)**(0.5)


def triangle(a):
    check(a)
    return ((16*a**2)/3)**(0.25)


def square(a):
    check(a)
    return a**(0.5)

def check(a):
    assert (float(a) >= 0), "Area cannot be negative"
    pass

if __name__ == "__main__":
    import sys
    assert (len(sys.argv) == 3), "There's something wrong with your imput: please indicate the type of shape, followed by its area."
    typ = sys.argv[1]
    area = float(sys.argv[2]) 
    assert (sys.argv[1] == 'TRIANGLE') or (sys.argv[1] == 'SQUARE') or (sys.argv[1] == 'CIRCLE'), "I\'m afraid the shape specified is not understood"
    side = 'side'
    if typ == 'CIRCLE':
        dim = str(circle(area))
        side = 'radius'
    elif typ == 'TRIANGLE':
        dim = str(triangle(area))
        typ = 'equilateral TRIANGLE'
    else:
        dim = str(square(area))
    print("{0}, area {1}, {2}: {3}".format( typ, area, side, dim))
