#!/usr/local/bin/python3

def checkdim(r : float) -> None:
    assert r >= 0, "Passed negative radius"
    pass

from math import pi

def area(r : float) -> float:
    checkdim(r)
    return pi*(r**2)

def perimeter(r : float) -> float:
    checkdim(r)
    return 2*pi*r


import sys

if __name__ == "__main__":
    r = float(sys.argv[1])
    print("area {}".format(area(r)))
    print("perimeter {}".format(perimeter(r)))

# Carl notes:
#  - potential for errors: it's fine for your code to have
#    "errors" - as in, produce errors, as long as they are
#    informative and not caused by an error in your code, but by user input
#  - casting via float will produce errors for strings
#  - assert let's you provide errors easily w/ custom message
#  - important think about code you reuse vs code you run directly
#  - python lets you do both in a script using if __name__ == "__main__" construct