#!usr/bin/python
from math import pi


circle = lambda a : (a/pi)**0.5
triangle = lambda a : 2*(a/(3**0.5))**0.5
square = lambda a : a**0.5


shapes = {'circle' : cicrle, 'triangle' : triangle, 'square' : square}
 
