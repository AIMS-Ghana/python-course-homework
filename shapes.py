#!/usr/bin/python

import sys
import math

def square_side(area):
	return math.sqrt(float (area))

def circle_radius(area):
	return math.sqrt(float(area)/math.pi)

def triangle_side(area):
	return (2*(float( area))**0.5)/3**0.25


def polygon_check(name, area):
    
    if name=='triangle':
        side= triangle_side(area)
        print 'Equilateral',name,'area',area, 'side:',side

    elif name=='square':
        side = square_side(area)
        print'SQUARE,', 'area',area, 'side:',side
    

    elif name== 'circle':
        radius=circle_radius(area)
        print 'CIRCLE,', 'area',area, 'radius:',radius

    else:
        print '... error indicating unknown shape...'






if __name__=="__main__":
    if len(sys.argv)==1:
        print('... error indicating no input...')
    else:
       polygon_check(sys.argv[1], sys.argv[2])

