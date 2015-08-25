#!/usr/bin/env python
import sys
import math
greeting="area= {0}, perimeter = {1}"

num1 = sys.argv[1]
# Add two numbers
sum = 2*math.pi*(float(num1))
product =math.pi*(float(num1))**2

# Display the sum
print('area {1}'.format(num1, product))
print('perimeter {1}'.format(num1, sum))
