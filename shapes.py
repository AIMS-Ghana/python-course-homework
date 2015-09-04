#!/usr/bin/env python
import sys
import math
import shape_objects

def polygon_check(polygon_name, area):
	
	if polygon_name.upper() =='TRIANGLE':
		#find side
                print shape_objects.Triangle(float(area)) #new changes to use the shape_object module
		'''
		side =(float(polygon_area*4) / float(math.sqrt(3)) )**(1/2)
		print '\nEquilateral TRIANGLE, area ', polygon_area, ', side: ',side,' .....\n'
		values = [polygon_area,side]
		return values
		'''
		
		
	elif polygon_name.upper()=='SQUARE':
		#find side
                print shape_objects.Square(float(area))
                '''
		side = math.sqrt(float(polygon_area))
		print '\nSQUARE, area ', polygon_area, ', side: ',side,' .....\n'
		values = [polygon_area,side]
		return values
 		'''

	
	elif polygon_name.upper() =='CIRCLE':
                print shape_objects.Circle(float(area))
                '''
		radius = math.sqrt(float(polygon_area)/math.pi)
		print '\nCIRCLE, area ', polygon_area, ', radius: ',radius,' .....\n'
		values = [polygon_area,radius]
		return values
                '''
	else:
		print '\n...error indicating unknown shape...\n'







if __name__ == "__main__":
	if len(sys.argv)==1:
		print '\n...error indicating no input...\n'
	else:
		polygon_check(sys.argv[1],sys.argv[2])


		












