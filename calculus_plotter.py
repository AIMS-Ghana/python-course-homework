#!/usr/bin/python

from pylab import *
import numpy
import math

X = arange(-5,6,0.001)
title("A graph of a function with it's derivative and integral")
xlabel("X")
ylabel("Y")
plot(X,sin(X), '--r', lw = 2, ms = 3, label = "f'(x)")
plot(X,cos(X), '--b', lw = 2, ms = 3, label = "f(x)")
legend()

