#!/usr/bin/python
import json
import math
import numpy
 



       ####### Creating a library for the various stages(Gillespie) ############

VarCond = { "infection":numpy.array([-1,1,0,0]),
	    "illness":numpy.array([0,-1,1,0]),
	    "recovery":numpy.array([0,0,-1,1]),
	    "mortE":numpy.array([1,-1,0,0]),
	    "mortI":numpy.array([1,0,-1,0]),
	    "mortR":numpy.array([1,0,0,-1])
}
		
def gSEIR(Y, t, mu, beta, sigma, gamma, N):
  S, E, I, R = Y
  infection = beta*S*I/N
  illness = sigma*E
  recovery = gamma*I
  mortE, mortI, mortR = mu*Y[1],mu*Y[2],mu*Y[3]
  rates = numpy.array([infection, illness, recovery, mortE, mortI, mortR])
  tot_rate = sum(rates)
  deltaT = numpy.random.exponential(1/tot_rate)
  WhichToChoose = numpy.random.choice(['infection', 'illness', 'recovery', 'mortE', 'mortI', 'mortR'], p = rates/tot_rate)
  return numpy.append(deltaT,Y+VarCond[WhichToChoose])





