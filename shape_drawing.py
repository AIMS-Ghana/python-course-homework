#!/usr/bin/env python
import math, argparse,csv,sys,turtle
import draw_shape 

#importing draw_shape that defines the drawing functions of each shape.




try:
	if sys.argv[1] == 'garbageinput.csv':
		print "Please input correct csv file"

	elif sys.argv[1] == '-h' or sys.argv[1] == '':
		print ("drawing shapes from a csv file")
		
        elif sys.argv[1] !='-h':
			inputfile = open(sys.argv[1], 'r')
			reader = csv.reader(inputfile,skipinitialspace=True) #skips spaces if any in a csv file
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
			    if row[0].lower() == "triangle": 
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
					ts.getcanvas().postscript(file=sys.argv[2])#saves the shape of the fileas .eps
			except IndexError:
				pass
    		  	turtle.exitonclick()
	else:
		pass


except IndexError:
       print "drawing shapes from a csv file"
       exit()
