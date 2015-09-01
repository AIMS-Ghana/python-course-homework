#!/usr/bin/env python
import sys
import math
greeting="area= {}, perimeter={}"

num1String = sys.argv[1]
num1=float(num1String)
#Add two numbers
summ = 2*math.pi*((num1))
product =math.pi*((num1))**2

# Display the sum
print(greeting.format(product, summ))
