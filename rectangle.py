#!/usr/local/bin/python3
import sys
greeting="larger,{0}!"
print(greeting.format(sys.argv[1]))
greenting="longuer,{1}!"
print(greeting.format(sys.argv[2]))
perimeter=sys.argv[1]+sys.argv[2]
print(greeting.format(perimeter))
area=sys.argv[1]*sys.argv[2]
print(greeting.format(area))
