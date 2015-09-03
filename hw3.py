#!/usr/bin/python3
import sys

no = len(sys.argv)
greeting = "hello {0}!"

if no == 1:
    print(greeting.format('world'))
elif no == 2:
    print(greeting.format(sys.argv[1]))
else:
    print(greeting.format(", ".join(sys.argv[1:-1]) + " and " + sys.argv[-1]))
