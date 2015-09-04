#!/usr/bin/python

def root(bisectf, rangex):
    	area = 0.0
   	for x in range(len(rangex)-1):
		a =bisectf(rangex[x])
		b =bisectf(rangex[x+1])
		c =(rangex[x+1]-rangex[x]/(b-a))
		d=(float(b*c))
		area=rangex[x+1]-d

	return area

	

               

#if __name__ == '__main__':
	

