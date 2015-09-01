#!/usr/bin/env python3

import sys
import random
import math

def rangef(a:float, b:float):
	a = int(a)
	b = int(b)
	return range(a,b)

a=sys.argv[1]
b=sys.argv[2]
count_inside = 0
for count in rangef(a ,b):
    d = math.hypot(random.random(), random.random())
    if d < 1: count_inside += 1
count += 1

count_inside1 = 0
for count1 in rangef(a ,b):
	g =  math.hypot(random.random(), random.random())
	if g < 1: count_inside1 +=1
count1 += 1

print("Circle-area pi:", 4.0 * count_inside / count , "\n Sphere- volume pi:",6.0 * count_inside1 / count1)
