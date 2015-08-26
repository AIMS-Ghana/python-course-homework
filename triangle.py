#!/use/bin/env python
import sys
greeting='area={0},perimeter={1}

num1 = sys.argv[1]
num2 = sys.argv[2]
num3 = sys.argv[3]
#Add two numbers
sum=(float(num1) + float(num2) + float(num3))
s = (float(num1) + float(num2) + float(num3))/2

#calulate the area
product = (s*(s-float(num1))*(s-float(num2))*(s-float(num3)))**0.5

#Displaythe
print('area {2}').format(num1, num2, product))
print('permeter {2}').format(num1, num2, sum))






