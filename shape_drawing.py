#!/usr/bin/env python
import turtle
import sys
import csv
import math
import draw_shape #importing shapes
import argparse

#drawing shapes and saving files as .eps


try:
	if sys.argv[1] == 'garbageinput.csv':
		print "Please input correct file, unable to read the garbageinput.csv file"

	elif sys.argv[1] == '-h' or sys.argv[1] == '': #checking for 1st argument
		print ("Drawing Realtime shapes using an input from a csv file")
		
        elif sys.argv[1] !='-h':
			inputfile = open(sys.argv[1], 'r')
			reader = csv.reader(inputfile,skipinitialspace=True) #checking for spaces in csv file
			for row in reader:
			    if int(row[2]) in range(0, 360):
				pass
                            else:
				print "Error, input rotation between 0 t0 360"
				exit()
			    if float(row[3])>0:
				pass
                            else:
				print "Error, input positive values only"
				exit()
			    if row[0].lower() == "triangle": #convets uppercase to lower case
				side=math.sqrt((float(row[3])*4)/math.sqrt(3))
				draw_shape.draw_triangle(side, str(row[1]), int(row[2]), float(row[4]), float(row[5]))
		
			    elif row[0].lower()=="square":
				side=math.sqrt(float(row[3]))
				draw_shape.draw_square(side, str(row[1]), int(row[2]), float(row[4]), float(row[5]))
		
			    elif row[0].lower()=="circle":
				radius=math.sqrt(float(row[3])/math.pi)
				draw_shape.draw_circle(radius, str(row[1]), int(row[2]), float(row[4]), float(row[5]))

			    elif row[0].lower()=="rectangle":
				side=float(0.618)*math.sqrt(float(row[3])/float(1.618))
				b=math.sqrt(float(row[3])/float(1.618))
				draw_shape.draw_rect(side,b, str(row[1]), float(row[2]),float(row[4]), float(row[5]))
			    else:
				pass

			
			
             	        try:
				if sys.argv[2]!='':				
					ts=turtle.getscreen()
					ts.getcanvas().postscript(file=sys.argv[2])
			except IndexError:
				pass
    		  	turtle.exitonclick()
	else:
		pass


except IndexError:
       print "Drawing Realtime shapes using an input from a csv file"
       exit()
