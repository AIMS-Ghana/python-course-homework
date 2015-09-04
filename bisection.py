#!/usr/bin/env python3

def root(f,rangex):
    tol = 10**(-8)
    begin, end = rangex[0], rangex[ len(rangex) - 1]
    mid = (begin + end)/2
    while abs(f(mid)) >= tol:
        if f(mid) > 0:
            end = mid
            mid = (begin + end)/2
        elif f(mid) < 0:
            begin = mid
            mid = (begin + end)/2
    return mid
