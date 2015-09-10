#!/usr/bin/env python
import json
import math
import numpy
 


#while (I0 > 0 and T0_range < t_max):


library = { "infection":numpy.array([-1,1,0,0]),
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
  which = numpy.random.choice(['infection', 'illness', 'recovery', 'mortE', 'mortI', 'mortR'], p = rates/tot_rate)
  return numpy.append(deltaT,Y+library[which])

dataSet = "SEIR.json"
for base_data in json.load(open(dataSet)):
	beta = base_data["beta"]
	sigma=base_data["sigma"]
	gamma=base_data["gamma"]
	mu=base_data["mu"]
	T0_end = base_data['t_max']
        S0,E0,I0,R0 = base_data["Y0"][0],base_data["Y0"][1],base_data["Y0"][2],base_data["Y0"][3]


  



