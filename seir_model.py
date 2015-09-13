#!/usr/bin/env python

#to calculate the seir model using the odient algorithm and the gillespie method on the same diagram.
#define the variables first assigning each variable and define the rates as well.
#formulate an arrray to explicitly show the order of sequence in the events.
#define the gillespie by outlining the conditions outlined.
#plot the the gillespie.
#finally outline the odient and plot it.
##

import json,os,sys,math
from scipy.integrate import odeint
import numpy as np
import scipy, scipy.integrate
import matplotlib.pyplot as plt
from pylab import *
import argparse


def ode(Y, t, beta, gamma,sigma, mu):
    
    S, E, I, R = Y
    N = sum(Y)
  
    #normal ODE
    illness = sigma*E
    infection = beta*S*I/N    
    #rates
    dS = mu * N - infection - mu * S
    dE = infection - illness - mu * E
    dI = illness - (gamma * I) - mu * I
    dR = gamma * I - mu * R
    dY = [ dS, dE, dI, dR ]
     
      
    return dY


events = {
  "infection" :np.array([-1, 1, 0, 0]),
  "illness": np.array([0,-1,1,0]),
  "recovery":np.array([0,0,-1,1]),
  "E_S":np.array([1,-1,0,0]),
  "I_S":np.array([1,0,-1,0]),
  "R_S":np.array([1,0,0,-1])
}

def gillespie(Y, t, beta, gamma,sigma, mu,N):
        S, E, I, R = Y
        
        infection  = beta*S*I/N    
        illness = sigma*E
        recovery = gamma * I
 	E_S = mu * Y[1]
        I_S = mu * Y[2]
        R_S = mu * Y[3]
        rates = np.array([infection,illness,recovery,E_S,I_S,R_S])
	tot_rate = sum(rates)
	deltaT = np.random.exponential(1/tot_rate)
	which_type = np.random.choice(['infection','illness','recovery','E_S','I_S','R_S'], p = rates/tot_rate) 
        return np.append(deltaT,Y + events[which_type])
   	
	

if len(sys.argv) >=2 and len(sys.argv)<=6:
        if str(sys.argv[1]) =='-h' or str(sys.argv[1]) =='-g':
		parser = argparse.ArgumentParser(description='plotting seir model')
		parser.add_argument('-g', type=str, dest='inp',
				   help='Run Gillespies model')
		args = parser.parse_args()
		print("\n", args, args.inp)

	else:
		filename, file_extension = os.path.splitext(str(sys.argv[1]))
		input_json = str(filename)+'.json'
		try:

			with open(input_json) as jsonfile:
				jsonData = json.load(jsonfile)
                           		
			Y0 =[]
			for n in jsonData['Y0']:
				if int(n)>=0:
					Y0 	= np.append(Y0,n)					
				else:
					print jsonData['Y0'], 'takes positive numbers only'
					exit()
			if float(jsonData['tmax'])>0:
				tMax 	= jsonData['tmax']
			else:
				print jsonData['tmax'],' takes positive numbers only'
				exit()
                        if float(jsonData['beta'])>=0:
				beta 	= jsonData['beta']
			else:
				print jsonData['beta'],' takes positive numbers only'
				exit()
			if float(jsonData['gamma'])>=0:
		        	gamma 	= jsonData['gamma']
			else:
				print jsonData['gamma'], ' takes positive numbers only'
				exit()
			if float(jsonData['sigma']) >=0:
				sigma   	= jsonData['sigma']
			else:
				print jsonData['sigma'],' takes positive numbers only'
				exit()
			if float(jsonData['mu']) >=0:
				mu 	= jsonData['mu']
			else:
				print jsonData['mu'],' takes positive numbers only'
				exit()

			N = sum(Y0)

			T = np.arange(0, tMax, 1)
                        solution = scipy.integrate.odeint(ode,
                                  Y0,
                                  T,
                                  args = (beta, gamma,sigma, mu))

                        S = solution[:, 0]
                        E = solution[:, 1]
			I = solution[:, 2]
			R = solution[:, 3]
			
			plt.figure()
			
			
			plt.plot(T,S,'-y')
			plt.plot(T,E,'-r')
			plt.plot(T,I,'-b')
			plt.plot(T,R,'-g')
                        R = 1

			try:
				if sys.argv[2] != '':
					if sys.argv[2] == '-g':
		                		R = int(sys.argv[3])
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
			run=1
			for i in range(R):
				deltaT = 0
				deltaT_list = np.array([deltaT])
				S_list = [Y0[0]]
				E_list = [Y0[1]]
				I_list = [Y0[2]]
				R_list = [Y0[3]]
				Y = Y0
                
				while(deltaT<tMax):  
				      values = gillespie(Y, deltaT,beta, gamma,sigma, mu,N)
				      Y = values[1:]
				      S_list = np.append(S_list,values[1])
				      E_list = np.append(E_list,values[2])
				      I_list = np.append(I_list,values[3])
				      R_list = np.append(R_list,values[4])
				      deltaT += values[0]
				      deltaT_list = np.append(deltaT_list, deltaT)
				      try:
                             			myfile_out.write(str(run)+','+str(Y[0])+','+str(Y[1])+','+str(Y[2])+','+str(Y[3]) +'\n')
                                                
				      except NameError:
						pass
				
				plt.step(deltaT_list,S_list,'-y')
				plt.step(deltaT_list,E_list,'-r')
				plt.step(deltaT_list,I_list,'-b')
				plt.step(deltaT_list,R_list,'-g')
				run +=1
			try:
				
				myfile_out.close()
			except NameError:
				pass
			plt.xlabel('Time')
			plt.ylabel('Proportion')

			plt.legend([ 'Susceptible', 'Exposed','Infected', 'Recovered' ])

			
		       
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
		except IOError as e:
		    print "\nI/O error({0}): {1}.\n start with name", input_json," in your directory!!\n".format(e.errno, e.strerror)


		except TypeError:
			print "Invalid data"

		


else:

	pass
