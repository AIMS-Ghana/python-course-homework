#!/usr/bin/python

import sys

def secant_solve(f,x1,x2,ftol,xtol):
  f1 = f(x1)
  if abs(f1) <= ftol : return x1        # already effectively zero
  f2 = f(x2)
  if abs(f2) <= ftol : return x2        # already effectively zero
  while abs(x2 - x1) > xtol :
    slope = (f2 - f1)/(x2 - x1)
    if slope == 0 :
      sys.stderr.write("Division by 0 due to vanishing slope - exit!\n")
      sys.exit(1)
    x3 = x2 - f2/slope               # the new approximate zero
    f3 = f(x3)                       # and its function value
    if abs(f3) <= ftol : break
    x1,f1 = x2,f2                    # copy x2,f2 to x1,f1
    x2,f2 = x3,f3                    # copy x3,f3 to x2,f2
  return x3

def quad(x):                  # a simple test function with known zeroes
  return  (x-5)*(x-2)
