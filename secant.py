#!/usr/bin/python

def root(funct, interval, TOL=1e-5, steps=100):
   a0, a1 = interval
   d = a1 - a0
   f0 = funct(a0)
   f1 = funct(a1)
   m = f1 - f0
   an = a1-f1*d/m
   fn = funct(an)

   if (fn <= TOL) or (steps == 0):
      return an
   else:
      return root(funct, [a1, an], TOL, steps)
