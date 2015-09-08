#!/usr/bin/python

def root(fxn, interval, tol=1e-5, steps=100):
    b0, b1 = interval
    d = b1 - b0
    f0 = fxn(b0)
    f1 = fxn(b1)
    m = f1 - f0
    bn = b1-f1*d/m
    fn = fxn(bn)
    if (fn <= tol) or (steps == 0):
        return bn
    else:
        return root(fxn, [b1, bn], tol, steps)
