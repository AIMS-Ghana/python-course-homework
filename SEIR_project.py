#!/usr/bin/python
import sys,os
import argparse
import scipy.integrate
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pylab as pl
from pylab import *
import json
import numpy as np
import gillespie_rates



if __name__ == "__main__":
	
		
	if len(sys.argv) >=2 and len(sys.argv)<=6:
		if str(sys.argv[1]) =='-h' or str(sys.argv[1]) =='-g':
			parser = argparse.ArgumentParser(description='This is a SEIR modelling program.This program calculates the dynamics for a SEIR system of differential equations and stochastic simulations of that same system (the Gillespie model). This program  accepts input in the form of a json file and optional output targets for numerical and plotted results.')
			parser.add_argument('-g', type=str, dest='inp',
					   help='Runs Gillespies model')
			args = parser.parse_args()
			print("\n", args, args.inp)
	
		else:

		        arith = str(sys.argv[1])
			
			for dataMain in json.load(open(arith)):
				beta = dataMain["beta"]
				sigma=dataMain["sigma"]
				gamma=dataMain["gamma"]
				mu=dataMain["mu"]
				T0_end = dataMain['t_max']
				S0,E0,I0,R0 = dataMain["Y0"]
			TS=1.0
			state =dataMain["Y0"]
			N= S0 + E0 + I0 + R0
	
                  ######## defining the main set of functions########

			def deff_eqns(state,t): 
				Y = np.zeros((4))
				V = state
				Y[0] = mu*N - (beta*V[0]*V[2])/N - mu*V[0]
				Y[1] = (beta*V[0]*V[2])/N - sigma*V[1] - mu*V[1]
				Y[2] = sigma*V[1] - gamma*V[2] - mu*V[2]
				Y[3] = gamma*V[2] - mu*V[3]

				return Y

		
		###########Get file name and extension##############

			filename, file_extension = os.path.splitext(str(sys.argv[1]))
			input_json = str(filename)+'.json'
			
	
			           		
		######## Initial condition ##########
			Y0 =[]
			for n in dataMain['Y0']:
				if int(n)>=0:
					Y0 	= np.append(Y0,n)
		
				else:
					print dataMain['Y0'], ' contains a negative number, provide a non-negative numbers only!!'
					exit()


			if float(dataMain['t_max'])>0:
				tMax 	= dataMain['t_max']
			else:
				print'Your maximum time within your json file is ', dataMain['t_max'],'which  is negative. Provide a non-negative number!!'
				exit()
			if float(dataMain['beta'])>=0:
				beta 	= dataMain['beta']
			else:
				print'Your beta value ', dataMain['beta'],' is negative, provide a non-negative value within the json file!!'
				exit()
			if float(dataMain['gamma'])>=0:
				gamma 	= dataMain['gamma']
			else:
				print'Your gamma value ', dataMain['gamma'],' is negative, provide a non-negative number value within the json file for gamma!!'
				exit()
			if float(dataMain['sigma']) >=0:
				sigma   	= dataMain['sigma']
			else:
				print'Your sigma value ', dataMain['sigma'],' is negative, provide a non-negative value for sigma within the json file. Thank you!!'
				exit()
			if float(dataMain['mu']) >=0:
				mu 	= dataMain['mu']
			else:
				print'Mu cannot be negative. Your mu value within the json file is ' ,dataMain['mu'],', provide a non-negative number!!'
				sys.exit()


		

		

			T0_start = 0.0
		        T0_end = dataMain['t_max']
		        T0_inc = TS
			T0_range = np.arange(T0_start, T0_end+T0_inc, T0_inc)
			RES = scipy.integrate.odeint(deff_eqns,state,T0_range)

			plt.plot(RES[:,0], '-g',label='Susceptibles')
			plt.plot(RES[:,1], '-m', label='Exposed')
			plt.plot(RES[:,2], '-r', label='Infectious')
			plt.plot(RES[:,3], '-k', label='Recovered')
			plt.title('SEIR results')
			plt.legend(loc=0)
			savefig('plot.png')
		
		
			########### This is the Gillispies method########
			NumStat = 1
			try:
				if sys.argv[2] != '':
					if sys.argv[2] == '-g':
						gN = int(sys.argv[3])
					else:
						try:
				                        
						    	filename, file_extension = os.path.splitext(str(sys.argv[2]))
							filecsv  = str(filename)+'.csv'
							print filecsv
							myfile_out = open(str(filecsv),'w')
							myfile_out.write('n,'+'t'+','+'S'+','+'E'+','+'I'+','+'R'+'\n')
							    
						except IndexError:
							pass
			
		
			except IndexError:
				pass
			try:
			    if sys.argv[4] !='':
				filename, file_extension = os.path.splitext(str(sys.argv[4]))
				filecsv  = str(filename)+'.csv'
				print filecsv
				myfile_out = open(str(filecsv),'w')
				myfile_out.write('n,'+'t'+','+'S'+','+'E'+','+'I'+','+'R'+'\n')
				    
			except IndexError:
				pass
			try:
				    if sys.argv[4] !='':
					filename, file_extension = os.path.splitext(str(sys.argv[4]))
					filecsv  = str(filename)+'.csv'
					myfile_out = open(str(filecsv),'w')
					   
			except IndexError:
				pass
			run =1
			for n in range(NumStat):
				deltaT =0
				deltaT_list = np.array([deltaT])
				S_list = [S0]
				E_list = [E0]
				I_list = [I0]
				R_list = [R0]
				while(deltaT<T0_end):  
				      values = gillespie_rates.gSEIR(state, deltaT, mu, beta, sigma, gamma, N)
				      state = values[1:]
				      S_list = np.append(S_list,values[1])
				      E_list = np.append(E_list,values[2])
				      I_list = np.append(I_list,values[3])
				      R_list = np.append(R_list,values[4])
				      deltaT += values[0]
				      deltaT_list = np.append(deltaT_list, deltaT)
				      try:
				      		myfile_out.write(str(state[0])+','+str(state[1])+','+str(state[2])+','+str(state[3]) +'\n')

				      except NameError:
						pass

				plt.step(deltaT_list, S_list, '-g')
				plt.step(deltaT_list, E_list, '-m')
				plt.step(deltaT_list, I_list, '-r')
				plt.step(deltaT_list, R_list, '-k')
				savefig('plot.png')
				run +=1
			try:
	
				myfile_out.close()
			except NameError:
				pass
			plt.xlabel('Time')
			plt.ylabel('Proportion')

			plt.legend([ 'Susceptible', 'Exposed','Infective', 'Recovered' ])

			# Actually display the plot

		       
			try:
			    if sys.argv[5] !='':
				filename, file_extension = os.path.splitext(str(sys.argv[5]))
				savefig(str(filename)+'.png')
			    										
			except IndexError:
				pass
			try:
				if sys.argv[2] != '-g':
					
					filename, file_extension = os.path.splitext(str(sys.argv[3]))
					savefig(str(filename)+'.png')
			except IndexError:
				pass

			plt.show()


		   
	 

