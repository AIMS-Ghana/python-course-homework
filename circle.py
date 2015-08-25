#!/usr/bin/python

import sys
area = " "
perimeter = " "

greeting = "area ={1} \n perimeter={1}"
a=sys.argv[1]
f=3.14*(int(a)^2)
h=2*3.14*(int(a))

area=str(f)
perimeter=str(h)
print(greeting.format(area, perimeter))
