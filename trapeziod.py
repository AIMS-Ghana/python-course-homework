#!/usr/bin/python


def integrate(bisectf, rangex):
	area = 0.0
   	for x in range(len(rangex)-1):
                w = (rangex[x+1]-rangex[x])


                fa=bisectf(rangex[x])
                fb=bisectf(rangex[x+1])
                
        	area = area + w*(fa+fb)/2
                return area


#if __name__ == "__main__":
	


