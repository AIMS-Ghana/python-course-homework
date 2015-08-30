#!/usr/bin/env python

#to calculate the midpoint,function to find integrators


def integrate(f, nbins):
    s=0

    for n in range(len(nbins)-1):
        width=nbins[n+1]-nbins[n]
        midp=float(nbins[n+1]+nbins[n]/2)
        height=f(midp)
        s=midp+width*height
    return s

