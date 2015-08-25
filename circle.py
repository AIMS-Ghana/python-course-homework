#!/usr/bin/python

import sys

import math

from math import pi

radius = float(sys.argv[1])


area = radius**2 * math.pi


perimeter=2*pi*radius

print"area "+str(area)
print"perimeter "+str(perimeter)

