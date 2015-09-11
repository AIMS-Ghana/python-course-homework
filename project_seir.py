#!/usr/bin/env python

'''
author=skamponsah
1. Calculate the dynamics for an SEIR system of differential equations and stochastic simulations of that same system(the Gillespie model)
2. Accept input from a json file
3. optional output targets for the numerical and plotted results

NB: S+E+I+R = N, dN/dt =0
    dS/dt = mu(N)-beta(SI)/N- mu(S)
    dE/dt = beta(SI)/N - sigma(E)-mu(E)
    dI/dt = sigma(E)-gamma(I)-mu(I)
    dR/dt = gamma(I)- mu(R)


OUTPUT:
  Either to a csv file or to the screen and should begin with a header line,follow with numerical values.
first line should be 0 followed by S0, E0, I0, R0 and tmax
final values should be S, E, I, R
    

tol =1e-6

'''

#########################################################################################################
import json
import os
import sys
import math
from scipy.integrate import odeint
import numpy as np
import scipy, scipy.integrate
import matplotlib.pyplot as plt
from pylab import *
import argparse



#########################################################################################################

#Using ODE
def derivs(Y, t, beta, gamma,sigma, mu):
    
    S, E, I, R = Y
    N = sum(Y)
  
    #normal ODE
    illness = sigma*E
    infection = beta*S*I/N    
    #calculations
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
  "mortE":np.array([1,-1,0,0]),
  "mortI":np.array([1,0,-1,0]),
  "mortR":np.array([1,0,0,-1])
}


#using Gellipse's method
def derivs_gm(Y, t, beta, gamma,sigma, mu,N):
        S, E, I, R = Y
        infection  = beta*S*I/N    
        illness = sigma*E
        recovery = gamma * I
 	mortE = mu * Y[1]
        mortI = mu * Y[2]
        mortR = mu * Y[3]
        rates = np.array([infection,illness,recovery,mortE,mortI,mortR])
	tot_rate = sum(rates)
	deltaT = np.random.exponential(1/tot_rate)
	which_type = np.random.choice(['infection','illness','recovery','mortE','mortI','mortR'],p = rates/tot_rate) 
        return np.append(deltaT,Y + events[which_type])
 
	
	
if __name__	==  "__main__":
	#Get input values
        if '-h' in sys.argv or len(sys.argv)==1:
		parser = argparse.ArgumentParser(description='Ode and Gillepsie methods')
		parser.add_argument('-g [N]', type=str, dest='gillepsie',
		help='arguments format [-g][N][target.csv][target.png]')
		args = parser.parse_args()
		print("\n", args, args.gillepsie)
		exit()
        if len(sys.argv) >=2 and len(sys.argv)<=6:
		if str(sys.argv[1]) =='-h' or str(sys.argv[1]) =='-g':
			pass

		else:
			#Get file name and extension
			filename, file_extension 	= os.path.splitext(str(sys.argv[1]))
			input_json 			= str(filename)+'.json'
			try:

				with open(input_json) as jsonfile:#open file
					jsonData 	= json.load(jsonfile)
		                   		
				# Initial condition// check if numbers are non-negative
				Y0 =[]
				for n in jsonData['Y0']:
					if int(n)>=0:
						Y0 	= np.append(Y0,n)
					
					else:
						print 'Y0 =',jsonData['Y0'], ' contains a negative number, provide a non-negative numbers only!!'
						exit()
			
				
				if float(jsonData['tmax'])>0:
					tMax 	= jsonData['tmax']
				else:
					print 'tmax = ', jsonData['tmax'],' is negative, provide a non-negative number!!'
					exit()
		                if float(jsonData['beta'])>=0:
					beta 	= jsonData['beta']
				else:
					print 'beta = ',jsonData['beta'],' is negative, provide a non-negative number!!'
					exit()
				
				if float(jsonData['sigma']) >=0:
					sigma   	= jsonData['sigma']
				else:
					print 'sigma =',jsonData['sigma'],' is negative, provide a non-negative number!!'
					exit()
                                if float(jsonData['gamma'])>=0:
					gamma 	= jsonData['gamma']
				else:
					print 'gamma = ', jsonData['gamma'],' is negative, provide a non-negative number!!'
					exit()
				if float(jsonData['mu']) >=0:
					mu 	= jsonData['mu']
				else:
					print 'mu = ',jsonData['mu'],' is negative, provide a non-negative number!!'
					exit()

				N = sum(Y0)

				T = np.arange(0, tMax, 1)
		                seir = scipy.integrate.odeint(derivs,
		                          			  Y0,
		                          			  T,
		                          			  args = (beta, gamma,sigma, mu))
		                S = seir[:, 0]
		                E = seir[:, 1]
				I = seir[:, 2]
				R = seir[:, 3]
			        if '-g' in sys.argv:
					pass
				else:
					out = open('out.csv','w')
					out.write('t,S,E,I,R\n')
    					for s in S:
						for e in E: 
                                                       for i in I:
                                                            for r in R:
					         	        out.write(str(s)+','+str(e)+str(i)+','+str(r)+'\n')#Write header of csv file
					out.close()
				#Plot graph using ODE method
				plt.figure()		
				plt.plot(T,S,'-b')
				plt.plot(T,E,'-y')
				plt.plot(T,I,'-r')
				plt.plot(T,R,'-g')
  
                                if  sys.argv[1] !='':
					

				        gN = 1 
					try:
						if sys.argv[2] != '':
							if sys.argv[2] == '-g':
								gN = int(sys.argv[3]) 
							else:
								try:
				                                        
								    	filename, file_extension = os.path.splitext(str(sys.argv[2]))
									filecsv  = str(filename)+'.csv'
									
									myfile_out = open(str(filecsv),'w')
									myfile_out.write('n,t,S,E,I,R\n')#Write header of csv file
									    
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
						myfile_out.write('n,t,S,E,I,R\n')
						    
					except IndexError:
						pass
                                         
					run=1# set initial number of run for gillepise
					for i in range(gN):
						deltaT = 0
						deltaT_list = np.array([deltaT])
						S_list = [Y0[0]]
						E_list = [Y0[1]]
						I_list = [Y0[2]]
						R_list = [Y0[3]]
						Y = Y0
				
						while(deltaT<tMax):  
						      values = derivs_gm(Y, deltaT,beta, gamma,sigma, mu,N)
						      Y = values[1:]
						      S_list = np.append(S_list,values[1])
						      E_list = np.append(E_list,values[2])
						      I_list = np.append(I_list,values[3])
						      R_list = np.append(R_list,values[4])
						      deltaT += values[0]
						      deltaT_list = np.append(deltaT_list, deltaT)
						      try:
				             			myfile_out.write(str(run)+','+str(values[0])+','+str(Y[0])+','+str(Y[1])+','+str(Y[2])+','+str(Y[3]) +'\n')
				                                
						      except NameError:
								pass
                                               
						if '-g' in sys.argv:
							plt.step(deltaT_list,S_list,'-b')
							plt.step(deltaT_list,E_list,'-y')
							plt.step(deltaT_list,I_list,'-r')
							plt.step(deltaT_list,R_list,'-g')
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
                                        savefig('plot.png')
					pass
		                try:
					if sys.argv[2] != '-g':
				                
						filename, file_extension = os.path.splitext(str(sys.argv[3]))
				                savefig(str(filename)+'.png')
				except IndexError:
                                        savefig('plot.png')
					pass
			
				plt.show()
			except IOError as e:
			    print "\nI/O error({0}): {1}.\n Please make sure you have with name", input_json," in your current directory!!\n".format(e.errno, e.strerror)


			except TypeError as e:
				print "\nI/O error({0}): {1}.\nFile contains invalid data record!!".format(e.errno,e.strerror)

		


	else:

		pass
