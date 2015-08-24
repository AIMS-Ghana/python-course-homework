#!/usr/local/bin/python3
import sys
greeting = "hello, {0}!"
word = "world"
if (len(sys.argv) == 2):
    word = sys.argv[1]
elif (len(sys.argv) > 2):
    word = ", ".join(sys.argv[1:-1]) + " and " + sys.argv[-1]
print(greeting.format(word))
# Carl keynotes:
#  - first introduction to conditionals, lists
#  - many tasks have a typical case covering most inputs, and an edge case or two
#  - desirable to have shared parts appear once (print(greeting.format(...))) and
#    logic for cases address only the moving target