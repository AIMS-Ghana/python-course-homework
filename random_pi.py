#!/usr/bin/python
from random import *
from math import sqrt, pi

quad = 0
s = 1000
for i in range(0, s):
    x = random()
    y = random()
    if sqrt(x * x + y * y) <= 1:
        quad += 1
Pi = 4*quad/s
print pi
 