#!/usr/bin/python

from numpy import*
import math
#def main():

rangex=linspace(0, 10, 100)
def integrate(f, rangex):
    #rangex=linspace(0, 10, 10, end ='True')
    Area = 0.0
    for k in rangex:
    #for x in range(len(rangex)-1):
        w = (rangex[k+1]-rangex[k])/2
        fa = float(rangex[0])
        fb = float(rangex[-1])
        h = f(float(fa + fb))
        Area = Area + h*w
    return Area

        #rangex=linspace(0, 10, 10, end ='True')
        #print(rangex)

if __name__=='__main__':main()
    
    
