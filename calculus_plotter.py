#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

def easy(x):

     return x

x1 = np.arange(0.0, 5.0, 0.1)
x2 = np.arange(0.0, 5.0, 0.02)
x3 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(x1, easy(x1))

#plt.figure(2)

plt.subplot(212)
plt.plot((x2)**2/2)
plt.show()

#plt.figure(3)

plt.subplot(213)
plt.plot((1))
plt.show()

'''
def exp_saturation(x):

    return 1 - np.exp(-x)
x1 = np.arange(0.0, 5.0, 0.1)
x2 = np.arange(0.0, 5.0, 0.02)
x3 = np.arange(0.0, 5.0, 0.1)

plt.figure(1)
plt.subplot(211)
plt.plot(1-np.exp(-x1))

plt.figure(2)
plt.subplot(212)
plt.plot(1-np.exp(-x2))

plt.figure(3)
plt.subplot(213)
plt.plot(x3 + np.exp(-x3))
plt.plot()
'''

