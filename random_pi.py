#!/usr/bin/python

import random
import math


count_inside = 0
for count in range(0, 10000):
    d = math.hypot(random.random(), random.random())
    if d < 1: count_inside += 1
count += 1
print 4.0 * count_inside / count


#print '%0.8f' % (4.0 * M / N)

count_inside = 0
for count in range(0, 10000):
    d = math.hypot(random.random(), random.random())
    if d < 1: count_inside += 1
count += 1
print 6.0 * count_inside / count


#print '%0.8f' % (4.0 * M / N)


