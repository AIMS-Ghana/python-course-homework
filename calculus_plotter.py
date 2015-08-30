#!/usr/bin/python
import math
import numpy as np
import matplotlib.pyplot as plt

t1 = np.arange(0, 90, 5)
y1 = np.sin(t1) + np.cos(t1)

t2 = np.arange(0, 90, 5)
y2 = np.cos(t2) - np.sin(t2)

t3 = np.arange(0, 90, 5)
y3 = np.sin(t3) - np.cos(t3)

#plots and axis titles and limits
plt.xlabel('t')
plt.ylabel('Y')
plt.title('A GRAPH OF Y AGAINST t')
plt.plot(t1, y1, 'r')
plt.plot(t2, y2, 'g')
plt.plot(t3, y3, 'y')
plt.show()

