#!/usr/bin/env python
import json
import math

dataSet = "SEIR.json"
for base_data in json.load(open(dataSet)):
	beta = base_data["beta"]
	sigma=base_data["sigma"]
	gamma=base_data["gamma"]
	mu=base_data["mu"]
	T0_end = base_data['t_max']
        S0,E0,I0,R0 = base_data["Y0"][0],base_data["Y0"][1],base_data["Y0"][2],base_data["Y0"][3]

N= S0 + E0 + I0 + R0
	
#while (I0 > 0 and T0_range < t_max):

def bsi(beta,S0,I0,N):
	return beta*S0*I0/N


def mu_rate(mu,S0,I0,N,R0,E0):
	return mu*(S0+I0+E0+N+R0)

def s_rate(E0):
	return sigma*E0

def g_rate(I0):
	return gamma*I0

#if __name__ == "__main__":
	#print (bsi(beta,S0,I0,N),mu_rate(mu,S0,I0,N,R0,E0),s_rate(E0),g_rate(I0))
def t_event(bsi, mu_rate,s_rate,g_rate):
	s=math.exp(bsi(beta,S0,I0,N)+mu_rate(mu,S0,I0,N,R0,E0)+s_rate(E0)+g_rate(I0))
	return s

