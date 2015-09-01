#!/usr/bin/python
import sys
n=len(sys.argv)
if n==0:
      print("hello word")
else:
       print ('hello'+' '+ sys.argv[n-1])
