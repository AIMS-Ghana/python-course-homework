#!/usr/bin/python3
import sys
import math
import numpy as np
import scipy as sp

import calculus_plotter as cp
import fun_plots as fp



for name in fp.funclist:


 cp.funcplot(name,[0,4,100])
