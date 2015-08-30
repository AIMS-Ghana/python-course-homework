#!/usr/bin/env python
import sys
import math
greeting="area= {}, perimeter = {}"

num1 = sys.argv[1]
# Add two numbers
UncleSam = 2*math.pi*(float(num1))
product =math.pi*(float(num1))**2

# Display the sum
print(greeting.format(num1, UncleSam))

