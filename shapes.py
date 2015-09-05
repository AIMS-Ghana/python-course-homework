#!/usr/bin/python
import math
import sys

def circle(area):
	return (area/math.pi)**0.5

def square(area):
	return area**0.5

def triangle(area):
	return 2*math.sqrt(area)/3**0.25



def shape(area, name):
    
        if name == 'CIRCLE':
    	    print name,' area: ', sys.argv[2],'radius:', circle(area) 
    	elif name == 'SQUARE':
     	   print name,' area: ', sys.argv[2],'side:', square(area) 
    	elif name == 'TRIANGLE':
           print 'equilateral ,', name,' area:',sys.argv[2],'side:',triangle(area) 
    	else:
	    print "...error indicating unknown shape..."

if __name__ == "__main__":
	
        if len(sys.argv) == 1:
          print "...error indicating no input..."
        else:
          area = float(sys.argv[2])
          name = sys.argv[1]

          shape(area,name)
	
        





   





