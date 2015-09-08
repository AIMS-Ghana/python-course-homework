#!/usr/bin/env python


import sys
import scipy.integrate as sci
import numpy as np
import pylab as pl
import json



dataSet = "SEIR.json"
for base_data in json.load(open(dataSet)):
	beta = base_data["beta"]
	sigma=base_data["sigma"]
	gamma=base_data["gamma"]
	mu=base_data["mu"]
	T0_end = base_data['t_max']
        S0,E0,I0,R0 = base_data["Y0"][0],base_data["Y0"][1],base_data["Y0"][2],base_data["Y0"][3]
	
                
TS=1.0
state =base_data["Y0"]
N= S0 + E0 + I0 + R0

def deff_eqns(state,t): # define the set of functions
	Y = np.zeros((4))
	V = state
	Y[0] = mu*N - (beta*V[0]*V[2])/N - mu*V[0]
	Y[1] = (beta*V[0]*V[2])/N - sigma*V[1] - mu*V[1]
	Y[2] = sigma*V[1] - gamma*V[2] - mu*V[2]
	Y[3] = gamma*V[2] - mu*V[3]

	return Y

#TS = t_inc
T0_start= 0.0; T0_end = 3; T0_inc = TS
T0_range = np.arange(T0_start, T0_end+T0_inc, T0_inc)
RES = sci.odeint(deff_eqns,state,T0_range)

Rec=1 - (RES[:,0]+RES[:,1]+RES[:,2]+RES[:,3])
print RES

#Ploting
pl.subplot(311)
pl.plot(RES[:,0], '-g', label='Susceptibles')
pl.title('SEIR results')
pl.xlabel('Time')
pl.ylabel('Susceptibles')
pl.subplot(312)
pl.plot(RES[:,1], '-m', label='Exposed')
pl.plot(RES[:,2], '-r', label='Infectious')
pl.legend(loc=0)
pl.xlabel('Time')
pl.ylabel('Infected')
pl.subplot(313)
pl.plot(Rec, '-k', label='Recovereds')
pl.xlabel('Time')
pl.ylabel('Recovereds')
pl.show()

