#!/usr/bin/python
# A program that prints a greeting statement
import sys
greeting = "hello {0}!"
word = " "

if len(sys.argv)==1:
    word = "World"

elif len(sys.argv) == 2:
    word = sys.argv[1]

else:
    word = " , ".join(sys.argv[1:-1]) + " and " + sys.argv[-1]

print (greeting.format(word))



