#!/usr/bin/python3

############SEIR model, odeint and Gillespie method##########

# uses input.json file ######################################

##### common imports #########################################


import sys
import math
import os

import json
import argparse

import numpy as np

import numpy.random as npr

from scipy import integrate
import matplotlib.pyplot as plt

################various functions##############################


############### argument parser ###############################


################ RHS for odeint ###############################



def dX_dt(X, t=0):
    
    S = X[0]
    I = X[1]
    R = X[2]

    dS = mu*(N-S) - beta*S*I/N
    dI = sigma*( N - S - R) - ( gamma + mu + sigma )*I
    dR = gamma*I - mu*R 

    return np.array([ dS , dI, dR ])


#################   plot   sols      #####################################

def lv_plot(S,E,I,R,t):
   
    
    plot1=plt.figure()
    plt.plot(t, S, 'k-', label='S')
    plt.plot(t, E  , 'b-', label='E')
    plt.plot(t, I  , 'r-', label='I')
    plt.plot(t, R  , 'c-', label='R')
    plt.grid()
    plt.legend(loc='best')
    plt.xlabel('time')
    plt.ylabel('S,E,I,R population fractions')
    plt.title('SEIR model')
    plt.show()
    
    return plot1

################  Gillespie      ##############################

def gillespie(X0,t,seed):
    
    import numpy.random as npr

    npr.seed(seed)

    S=X0[0]
    I=X0[1]
    R=X0[2]
    E=N - S - I - R

    t0 = t[0]
    tfinal = t[-1]
    t = t0 

    Sout=[S]
    Eout=[N-S-I-R]
    Iout=[I]
    Rout=[R]
    Tout=[t]
   
    while t < tfinal:

        L =  beta*S*I/N  +sigma*E   +  gamma*I + mu*R +mu*I + mu*E

        twait = npr.exponential(1/L)         # exponentially distributed waiting time, parameter 1/L

        
        prob_SE =  beta*S*I/(L*N) 
        
        prob_EI = sigma*E/L
        
        prob_IR = gamma*I/L
        
        prob_RS = mu*R/L

        prob_IS = mu*I/L

        prob_ES = mu*E/L
    

        p =[prob_SE, prob_EI, prob_IR,prob_RS, prob_IS, prob_ES]

        #print("before",S,E,I,R) # test that updater is working as planned
        
        chooser =  npr.choice(["SE","EI","IR","RS","IS","ES"],1,p=p) # pick S+,S- etc 
       
        # function for each of SE,EI,IR,etc etc

        update_switch ={
                    "SE" : lambda S,E,I,R: (S-1,E+1,I,R),
                    "EI" : lambda S,E,I,R: (S,E-1,I+1,R),
                    "IR" : lambda S,E,I,R: (S,E,I-1,R+1),
                    "RS" : lambda S,E,I,R: (S+1,E,I,R-1),
                    "IS" : lambda S,E,I,R: (S+1,E,I-1,R),
                    "ES" : lambda S,E,I,R: (S+1,E-1,I,R)
                    
     	}
                
        # run update with correct function

        def updater(S,E,I,R):
          return update_switch[chooser[0]](S,E,I,R)

        #print("before",S,E,I,R)
        
        (S,E,I,R) = updater(S,E,I,R)

        #print("after",S,E,I,R) # test that updater is working as planned

        t = t + twait
   
        
        
        Sout.append(S)
        Eout.append(E)
        Iout.append(I)
        Rout.append(R)
        Tout.append(t)
    
    return Sout,Eout,Iout,Rout,Tout





#############################################################################
################   Main prog      ###########################################
#############################################################################

if __name__ == "__main__":


##############  paramter,ic input      #######################################

    input_args=json.load(open(sys.argv[1]))
    
    
        
    X0 =  input_args['X0']     # initials conditions: reasonably sane

    mu =  input_args['mu'] 
    beta = input_args['beta'] 
    sigma = input_args['sigma']
    gamma =  input_args['gamma']

    N = input_args['N']                    # population size
    tmax = input_args['tmax']              # enough time to see something happen


###############   hardwired input for testing, odeint/Gillespie #####################
    #  input json file should provide these
                  
    # X0 = np.array([0.90, 0.01, 0.08, 0.01])      # initials conditions: reasonably sane


 
    # mu =  0.1
    # beta = 10.0
    # sigma = 1.0
    # gamma = 1.0

    # N = 1000
    # tmax = 20                             # enough time to see something happen

##################   odesolver   ################################################# 

    t = np.linspace(0, tmax,  10000)            # could make stepno a variable too

    X = integrate.odeint(dX_dt, X0, t)          # run the diff eq. solver



################### Gillespie ####################################################

    seed = 1
    S = X[:,0]                    # mangle to feed into Gillespie (written earlier for LV)
    I = X[:,1]
    R = X[:,2]
    E = N - S - I - R

   

    Sout,Eout,Iout,Rout,Tout=gillespie(X0,t,seed)   
 
################## run Niter Gillepsies ##########################################
 #   Niter = 5

    
    

  #  for i in range(0,Niter):
  #    seed = npr.rand()
  #    S[i] = X[:,0]                    # mangle to feed into Gillespie (written earlier for LV)
  #    I[i] = X[:,1]
  #    R[i] = X[:,2]
  #    E[i] = N[i] - S[i] - I[i] - R[i]
  #    Sout[i],Eout[i],Iout[i],Rout[i],Tout[i]=gillespie(X0,t,seed) 

  
    

    


################### Plots #########################################################

    fig1 = lv_plot(S,E,I,R,t)                         # plot results, odeint
       

    fig2 = lv_plot(Sout[:-1],Eout[:-1],Iout[:-1],Rout[:-1],Tout[:-1])    # plot results gillespie


    fig1.show()
    

    fig1.savefig("SEIRode.png")      

    fig2.show()

    fig2.savefig("SEIRgillespie.png")

    
