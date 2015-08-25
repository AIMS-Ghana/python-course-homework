#!/usr/bin/env python
import sys
greeting="area= {0}, perimeter = {1}"

num1 = sys.argv[1]
num2 = sys.argv[2]
# Add two numbers
sum = (float(num1) + float(num2))*2
product =(float(num1))*(float(num2))

# Display the sum
print('area {2}'.format(num1, num2, product))
print('perimeter {2}'.format(num1, num2, sum))



