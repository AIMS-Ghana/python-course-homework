#!/usr/local/bin/python3
import sys
greeting = "hello, {0}!"
print(greeting.format(sys.argv[1]))

# Carl keynotes: need to know how to get program arguments
#  - formatted strings `string.format(...)` in Python, sprintf in many other languages,
#    is another universal need.