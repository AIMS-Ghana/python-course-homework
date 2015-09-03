import csv
import sys


def read(name):
	sum=0.0
	count=0
	f = open(name)
	for line in f:
	    colunm = line.split(',')

	    if len(colunm) >=1:

		if 'educational' in colunm[5]:
			fund=float(colunm[0].replace('"',''))
			sum=sum+ fund 
			count=count+1
			#print colunm[0]
	    else:
		print "NO educational fees found."
	
	print " The total amount of funds requested for education is: ",sum
	f.close()

if __name__ == "__main__":
	name=str(sys.argv[1])
	read(name)

