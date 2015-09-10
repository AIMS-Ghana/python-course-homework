#!/usr/bin/env python
import sys
import math
import shape_objects
import turtle

def polygon_check(polygon_name,fill,degree,area,x_org,y_org):
	
	if polygon_name.upper() =='TRIANGLE':
		#find side
                tri = shape_objects.Triangle(float(area))
                print tri #new changes to use the shape_object module
                tri.draw(turtle,fill,degree,x_org,y_org)
    		
                
		'''
		side =(float(polygon_area*4) / float(math.sqrt(3)) )**(1/2)
		print '\nEquilateral TRIANGLE, area ', polygon_area, ', side: ',side,' .....\n'
		values = [polygon_area,side]
		return values
		'''
		
		
	elif polygon_name.upper()=='SQUARE':
		#find side
                sqr = shape_objects.Square(float(area))
                print sqr
                sqr.draw(turtle,fill,degree,x_org,y_org)
    		
                '''
		side = math.sqrt(float(polygon_area))
		print '\nSQUARE, area ', polygon_area, ', side: ',side,' .....\n'
		values = [polygon_area,side]
		return values
 		'''

	
	elif polygon_name.upper() =='CIRCLE':
                circ = shape_objects.Circle(float(area))
                print circ
    		circ.draw(turtle,fill,degree,x_org,y_org)
                '''
		radius = math.sqrt(float(polygon_area)/math.pi)
		print '\nCIRCLE, area ', polygon_area, ', radius: ',radius,' .....\n'
		values = [polygon_area,radius]
		return values
                '''

	elif polygon_name.upper() =='RECTANGLE':
                rect = shape_objects.Rectangle(float(area))
                print rect
    		rect.draw(turtle,fill,degree,x_org,y_org)
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


		












