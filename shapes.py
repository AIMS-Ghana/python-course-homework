#!/usr/local/bin/python3
import math, sys
greeting= "{0}"
word=" "
def caltrin(area):
 k=(4*area)/(math.sqrt(3))
 tr=math.sqrt(k)
 word="TRIANGLE, area "+str(area) +" ,Side:"+str(tr)
 print (greeting.format(word))
 return tr

def calsqr(area):
 sqr=math.sqrt(area)
 word="SQUARE, area "+str(area) +" ,Side:"+str(sqr)
 print (greeting.format(word))
 return sqr

def calcir(area):
 p=math.pi
 c=float(area/p)
 cir=math.sqrt(c)
 word="CIRCLE, area "+str(area) +" ,radius:"+str(cir)
 print (greeting.format(word))
 return cir

if __name__ == "__main__": 
	if (len(sys.argv))==(1):
	  print ("... error indicating no input...")
	elif str(sys.argv[1])=="TRIANGLE":
	  print(caltrin(int(sys.argv[2])))
	elif str(sys.argv[1])=="SQUARE":
	  print(calsqr (int(sys.argv[2])))
	elif str(sys.argv[1])=="CIRCLE":
	  print(calcir(int(sys.argv[2])))
	else:
	  print("Sorry ... check your input")



	 

 

