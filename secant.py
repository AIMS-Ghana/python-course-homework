#!/usr/bin/python

def root(f, interval, tolerance=1e-5, steps=100):
    x0, x1 = interval
    d = x1 - x0
    f0 = f(x0)
    f1 = f(x1)
    mid = f1 - f0
    xn = x1-f1*d/mid
    fn = f(xn)
    if (fn <= tolerance) or (steps == 0):
        return xn
    else:
        return root(f, [x1, xn], tolerance, steps)	

