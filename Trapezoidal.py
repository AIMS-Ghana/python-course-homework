
def integrate(intf, rangex, steps=1000.0):
  
  tol=".0001"
 # n=float((b-a)/steps)
  #h = float((b-a)/2)
  sum = 0.0
  for n in range(len(rangex)-1):
        a=rangex[n]
        b=rangex[n+1]
   	h1=intf(a)
  	h2 =intf(b)
        width=b-a
        sum += width*(h1+h2)/2
  return sum
