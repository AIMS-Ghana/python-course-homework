#!/usr/bin/python
def root(f,ab, eps=1e-5, depth=100):
  a = ab[0]
  b = ab[1]
  assert f(a)*f(b)<0, "f(a) "+str(a)+" and f(b) "+str(b)+" do not have opposite signs"
  x=(a+b)/2.0
  fx = f(x)
  if (abs(fx) <= eps) or (depth == 0): 
    return x
  else:
    if fx*f(a)<0:
      return root(f,[a,x],eps,depth-1)
    else:
      return root(f,[x,b],eps,depth-1)

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
