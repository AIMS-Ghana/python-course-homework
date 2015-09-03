 #!/usr/bin/python
import math
def root(bisectf, rangex):
 p0=rangex[0]
 p1=rangex[-1]
 tol=".001"
 steps="10000"
 i = 2
 q0 = bisectf( p0 )
 q1 = bisectf( p1)
 while i <= steps :
	k1=(p1-p0)
	k2=(q1 - q0)
	p = p1 - (q1*(k1/k2))
 	if abs(p - p1) < tol:
		return p
	else:
		i=i+1
		p0=p1
		q0=q1
		p1=p
		q1=bisectf(p)



