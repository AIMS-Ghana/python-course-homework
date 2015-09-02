

import sys
from random import *
 
N = int(sys.argv[2])
total = 0
TOTAL = 0
for i in range (0, N):
    t = random ()
    h = random ()
    if t**2 + h**2 <= 1:
        total = total + 1
   
print "circle-area pi : {}".format(float(4*total)/N)
for i in range (0, N):
    j = random ()
    n = random ()
    m = random () 
    if j**2 + n**2 + m**2 <=1:
        TOTAL = TOTAL + 1
print "sphere-volume pi : {}".format(float(6*TOTAL)/N)
