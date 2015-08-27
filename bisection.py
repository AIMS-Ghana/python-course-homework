#!/usr/bin/python
TOL = 0.001
def root(f, *rangx):
    a, b = rangx
    assert isinstance(a, float) & isinstance(b, float), "Function requires a float"
    assert f(a)*f(b)< 0, "Bisection method cannot be implemented"
    while (b-a)/2.0 > TOL : 
          m = (a + b)/2
          if f(m) == 0:
              return m
          if f(a)*f(m) < 0:
              b = m
          else: a = m
          m = (a+b)/2
    return c
 
