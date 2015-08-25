#!/usr/bin/python
import sys
import math
result = "area = {0}, perimeter = {1}"
a=float (sys.argv[1])
b=float (sys.argv[2])
c=float (sys.argv[3])
#add three numbers
m=(a+b+c)/2
sum = a+b+c
product = (m*(m-a)*(m-b)*(m-c))**0.5
# display sum
print(result. format(product,sum))


