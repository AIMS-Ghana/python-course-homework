#!/usr/bin/python3
# This uses the sys module to obtain arguments from the command line.
# Note that arguments are always imported as strings.


import sys
print('hello, {0}!'.format(str(sys.argv[1])))


