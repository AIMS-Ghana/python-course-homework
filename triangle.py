#!/usr/bin/python
import sys

var1 = eval (sys.argv[1])
var2 = eval (sys.argv[2])

area = var1 * var2
perimeter = (2 * var1) + (2* var2)

print "Area ,",area
print "Perimeter ,",perimeter

