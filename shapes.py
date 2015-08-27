#!/usr/bin/python3
import maths
import sys
if __name__ == "main":
	def side():
		if len (sys.argv) < 3:
          		print "variables incomplete"
			elif len (sys.argrv) ==3:	
	 		str (sys.argv[1]) == "TRIANGLE" 
         		side = math.sqrt (4*(sys.argv[2])/math.sqrt(3))
			print ("equilateral TRIANGLE, area {} , side.. {}".format (side) ) 
			str(sys.argv[1]) == "CIRCLE"
			side = float (math.sqrt(sys.argv[2]/math.pi))
			print ("CIRCLE, area {} , radius {}".format (side))
			str(sys.argv [1]) == "SQUARE"
			side = float (math.sqrt(sys.argv[2]))
			print ("SQUARE, area {} , side {}".format (side))
			return side


    
          
			else:
			print "check variables"
