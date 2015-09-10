#!/usr/bin/env python
'''

1. draw shapes of different sizes and different colors at different locations
2. Overlapping each other at a single point
3. Accept input from a csv file for each shape to draw
4. Optionally output the results of the figures draws"
5.  Content of the csv file: 
	i: SHAPE,COLOR,(0,360),AREA, x-origin,y-origin,
	  if GOLDEN RECTANGLE, EQUILATERAL TRIANGLE,SQUARE, CIRCLE

6. Error handling
	i. Invalid csv file name
	ii. Invalid data input for csv file, though correct name
        
7. Save output as .eps if output file name is provided
8. run code in real time
9. end program

'''

##########################################################################################################################################
#Imports
import shapes
import csv
import os
import sys
import turtle
from Tkinter import *
import argparse

if len(sys.argv)==2 or len(sys.argv)==3:
        if str(sys.argv[1]) == "-h":
		
		parser = argparse.ArgumentParser(description='Drawing Shapes Code.')
		parser.add_argument('-input-csv', type=str, dest='input',
				   help='an input file')
		args = parser.parse_args()
		print("\n", args, args.inp)

	else:
		#Get file name and extension
		filename, file_extension = os.path.splitext(str(sys.argv[1]))
		input_csv = str(filename)+'.csv'
		
		try:

			with open(input_csv,'r') as csvfile:#open file
				inputData = csv.reader(csvfile,delimiter=',', quotechar='"')
		                next(inputData)
		                turtle.Screen().title("Welcome to My Project Shapes!")
		                turtle.setup(10000, 1000)
                                turtle.speed(500)
                                try:
					for line in inputData:
                                            print(len(line))
				            shapes.polygon_check(line[0],str(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]))
				except csv.Error as e:
					sys.exit('file %s, line %d: %s' % (filename, inputData.line_num, e))
				#capture screen and save if output file is provided
		                if  len(sys.argv)==3:
		                	output_filename, extension = os.path.splitext(str(sys.argv[2]))
		                	ts = turtle.getscreen()
		                	ts.getcanvas().postscript(file=str(output_filename)+".eps")
                                ###########################################################################
				#additional Drawings
				'''
                                smiles = turtle.Turtle()    
				smiles.penup()
				smiles.goto(-75,150)
				smiles.pendown()
				smiles.circle(10)     #eye one

				smiles.penup()
				smiles.goto(75,150)
				smiles.pendown()
				smiles.circle(10)     #eye two

				smiles.penup()
				smiles.goto(0,0)
				smiles.pendown()
				smiles.circle(100,90)   #right smile

				smiles.penup()           
				smiles.setheading(180) # <-- look West
				smiles.goto(0,0)
				smiles.pendown()
				smiles.circle(-100,90)
				'''
		                turtle.Screen().exitonclick()
		except IOError as e:
		    print "\nI/O error({0}): {1}.\n Please make sure you have with name", input_csv," in your current directory!!\n".format(e.errno, e.strerror)
else:
	pass
    

if __name__ == "__main__":
	pass







