#!/usr/bin/python

def integrate(f, rangex):
    area = 0.0
    for x in range(len(rangex)-1):
        w = (rangex[x+1] - rangex[x])
        fa = float(rangex[x])
        fb = float(rangex[x+1])
        h = f(float(fa + fb))
        area2 = area + h*w
        return area2



