#!/usr/bin/env python
import sys
import math


def polygon_check(polygon_name, polygon_area):
	
	if polygon_name.upper() =='TRIANGLE':
		#find side
		side = math.sqrt(float(polygon_area*4)/ float(math.sqrt(3)))
		print '\nEquilateral TRIANGLE, area ', polygon_area, ', side: ',side,' .....\n'
		
		
	elif polygon_name.upper()=='SQUARE':
		#find side
		side = math.sqrt(float(polygon_area))
		print '\nSQUARE, area ', polygon_area, ', side: ',side,' .....\n'
	
	elif polygon_name.upper() =='CIRCLE':
		radius = math.sqrt(float(polygon_area)/math.pi)
		print '\nCIRCLE, area ', polygon_area, ', radius: ',radius,' .....\n'
	else:
		print '\n...error indicating unknown shape...\n'


if __name__ == "__main__":
	if len(sys.argv)==1:
		print '\n...error indicating no input...\n'
	else:
		polygon_check(sys.argv[1],sys.argv[2])


		












