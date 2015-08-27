#!/usr/bin/python3

import bisection

def bisectf(x):
    f = raw_input('write a function involving x (example (x-1)(x+10)**2)')
    code = 'g = lambda x: {}'.format(f)
    exec(code)
    return g(x)

rangex = (0.0, 10.0)

print(bisection.root(bisectf, *rangex))
