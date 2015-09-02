#!/usr/bin/python

import sys
9
def f(x):
	return x**3 + x -1
	
<<<<<<< Updated upstream
<<<<<<< Updated upstream
def root(a:float,b:float,tol=.0001):
=======
def Root(a:float,b:float,tol=.0001):
>>>>>>> Stashed changes
=======
def Root(a:float,b:float,tol=.0001):
>>>>>>> Stashed changes
	c = (a + b)/2.0
	while (b-a)/2.0 > tol:
		if f(c) == 0:
			return c
		elif f(a)*f(c) < 0:
			b = c
		else :
			a = c
		
	return c
	
def main(argv):
	if (len(sys.argv) != 4):
		sys.exit('Usage: bisection.py <a> <b> <tol>')
	else:
		print("The root is:")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
		print ('{}'.format(root( int(sys.argv[1]) , int(sys.argv[2]))))
=======
		print ('{}'.format(Root( int(sys.argv[1]) , int(sys.argv[2]))))
>>>>>>> Stashed changes
=======
		print ('{}'.format(Root( int(sys.argv[1]) , int(sys.argv[2]))))
>>>>>>> Stashed changes

if __name__ == "__main__":
	main(sys.argv[1:])
        
