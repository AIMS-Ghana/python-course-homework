#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import fun_plots


t = np.arange(0.0, 5.0, 0.01)
s = fun_plots.sine_and_cos(t)
line, = plt.plot(t,s,lw=2)

plt.ylim(-2,2)
plt.show()
