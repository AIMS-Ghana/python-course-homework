#!/usr/local/bin/python3
import sys
greeting = "hello, {0}!"
who = "world"
if (len(sys.argv) == 2):
    who = sys.argv[1]
elif (len(sys.argv) > 2):
    who = ", ".join(sys.argv[1:-1]) + " and " + sys.argv[-1]
print(greeting.format(who))
# Carl keynotes:
#  - first introduction to conditionals, lists
#  - many tasks have a typical case covering most inputs, and an edge case or two
#  - desirable to have shared parts appear once (print(greeting.format(...))) and
#    logic for cases address only the moving target