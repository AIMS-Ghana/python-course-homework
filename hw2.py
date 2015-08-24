#!/usr/bin/env python
import sys 

input_var = sys.argv[1]

def greetings(word=input_var):
	print 'hello,', word,'!'

if __name__ == "__main__":
	greetings()



