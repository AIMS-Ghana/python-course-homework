#!/usr/bin/python3

import sys
greet = "Hello, {0}!"
word = " "
if len(sys.argv) == 1:
 word = "World"
elif len(sys.argv) == 2:
 word = sys.argv[1]
else:
 word = ",".join(sys.argv[1:-1]) + " and " + sys.argv[-1]

print(greet.format(word))
