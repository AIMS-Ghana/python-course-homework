#!/usr/bin/python

def integrate(f, rangex):
    area = 0.0
    for k in range(len(rangex)-1):
        width = rangex[k+1]-rangex[k]
        height = f(float((rangex[k+1]+rangex[k])/2))
        area += height*width
	
    return area

#if __name__ == '__main__':
	
