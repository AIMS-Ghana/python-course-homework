#!/usr/bin/python3

import sys

no = len(sys.argv) - 1
greeting = "hello {0}!"

if no == 0:
    print(greeting.format('World'))
elif no == 1:
    print(greeting.format(sys.argv[1]))
else:
    add = ''
    for i in range(no-1):
        add = add + sys.argv[1+i] + ', '
    add = add + 'and '+ sys.argv[no]
    print(greeting.format(add))
