#!/usr/bin/python
import scipy, scipy.integrate
import numpy
from collections import namedtuple
Params = namedtuple('Params','beta sigma mu gamma ')
beta=0.5
gamma=0.2
sigma=2
mu=1/2


S, E, I, R = 0.9, 0, 0.1, 0

Y = (S, E, I, R)

tMax = 100

T = numpy.linspace(0,tMax,1000,endpoint=True)

def dSEIR(Y, t):
    S,E,I,R = Y
    N = S + E + I + R

    infection = (beta * S * I)/N
    #disease = ...
    #recover = ...
    #mortI, mortE, mortR = ...

    dS = mu * N - infection - mu * S
    dE = infection - sigma * E - mu * E
    dI = sigma * E -gamma * I - mu * I
    dR = gamma * I - mu * R

    return [ dS, dE, dI, dR ]


solution= scipy.integrate.odeint(dSEIR,Y,T)


S = solution[:,0]
E = solution[:,1]
I = solution[:,2]
R = solution[:,3]


json.load(open(""))

import pylab

pylab.figure()

pylab.plot(T, S,
           T, E,
           T, I,
           T, R)

pylab.xlabel('Time')
pylab.ylabel('Proportion')

pylab.legend(['Susceptible','Exposed', 'Infective', 'Recovered' ])

pylab.show()

