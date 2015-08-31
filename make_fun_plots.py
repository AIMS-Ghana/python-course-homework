#!/usr/bin/python

import matplotlib.pyplot as plt

import calculus_plotter, fun_plots

from numpy import *

for i in arange(0,5):
  calculus_plotter.plot_all(fun_plots.funclist[i],
  arange(0,10,0.01))
    
