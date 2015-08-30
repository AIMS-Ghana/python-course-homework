
def integrate(intf, rangex, steps=10000.0):
  a=rangex[0]
  b=rangex[-1]
  tol=".0001"
  

  h = float((b-a)/steps)
  sum = 0.0
  x = a + h                 
  while (x < b):
        sum=sum+ h * intf(x)
        x =x+h

  return sum
