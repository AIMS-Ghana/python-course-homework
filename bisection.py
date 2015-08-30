#!/usr/bin/python
def root(f,ab, eps=1e-5, depth=100):
   a = ab[0]
   b = ab[1]
  assert f(a)*f(b)<0, "f(a) "+str(a)+" and f(b) "+str(b)+" do not have opposite signs"
 
def root2(f,ab,eps=1e-5,depth=100):
   a = ab[0]
   b = ab[1]
   fa = f(a)
   fb = f(b)
  assert fa*fb<0, "f(a) "+str(a)+" and f(b) "+str(b)+" do not have opposite signs"
   x=(a+b)/2.0
   fx = f(x)
  while ((abs(fx) > eps) or depth > 0):
    if fx*fa<0:
    b = x
    fb = fx
    else:
    a = x
    fa = fx
    x=(a+b)/2.0
    fx = f(x)
    

if __name__ == "__main__":
    def func(x):
    return (x**2-5)
  print(str(root(func,[2,3])))
