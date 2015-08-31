#!/usr/bin/python

import sys
import math


def triangle_side(area):
    return (2*(float( area))**0.5)/3**0.25

def square_side(area):
    return math.sqrt(float (area))

def circle_radius(area):
    return math.sqrt(float(area)/math.pi)

def polygon_check(name,area):
    
    if name=='TRIANGLE':
        side= triangle_side(area)
        print("Equilateral {0}, area {1}, side: {2}").format(name,area,side)
    
    elif name=='SQUARE':
        side = square_side(area)
        print("{0}, area {1}, side: {2}").format(name,area,side)
    

    elif name=='CIRCLE':
        radius=circle_radius(area)
        print("{0}, area {1}, radius: {2}").format(name,area,radius)

    else:
        print('... error indicating unknown shape... ')

	

if __name__=="__main__":

    if len(sys.argv)==1:
        print('... error indicating no input...')
    else:
        polygon_check(sys.argv[1], sys.argv[2])

