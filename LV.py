#!/usr/bin/python3
import sys
import math

import numpy as np

from scipy import integrate
import matplotlib.pyplot as plt


################ RHS for odeint ###############################



def dX_dt(X, t=0):
    
    x=X[0]
    y=X[1]

    dx=(a*x) - (b*x*y)
    dy=(-c*y) + (d*x*y)

    return np.array([ dx , dy ])


#################   plot   sols      #####################################

def lv_plot(prey,pred,t):
   
   
    plt.figure()
    plt.plot(t, prey, 'r-', label='Prey')
    plt.plot(t, pred  , 'b-', label='Predators')
    plt.grid()
    plt.legend(loc='best')
    plt.xlabel('time')
    plt.ylabel('numbers')
    plt.title('Predator and prey populations')
    
    plt.show()
################ plot phase #############################################

def lv_plot_phase(prey,pred):

    plt.figure()
    plt.plot(pred, prey, 'r-', label='Phase Plot')
    plt.grid()
    plt.legend(loc='best')
    plt.xlabel('pred')
    plt.ylabel('preys')
    plt.title('Predator and prey phase plot')   


    plt.show()
################  Gillespie it       ##############################

def gillespie(X0,t,seed):
    
    import numpy.random as npr

    npr.seed(seed)

    x=X0[0]
    y=X0[1]
    t0=t[0]
    tfinal = t[-1]
    t = t0 

    xout=[x]
    yout=[y]
    tout=[t]
    
   
    while t < tfinal:

        L = a*x+ c*y + x*y*(b + d)           

        twait = npr.exponential(1/L)         # exponentially distributed waiting time, parameter 1/L

        prob_xp = a*x/L                      # probability an x+ fires in [0,twait]
        prob_xm = b*x*y/L
        prob_yp = d*x*y/L
        prob_ym = c*y/L
    

        p =[prob_xp, prob_xm, prob_yp, prob_ym]

        #print("before",x,y) # test that updater is working as planned
        
        chooser =  npr.choice(["xp","xm","yp","ym"],1,p=p) # pick x+,x-,y+,y- with appropriate weighted prob
       
        # function for each of x+,x-,y+,y-

        update_switch ={
                    "xp" : lambda x,y: (x+1,y),
                    "xm" : lambda x,y: (x-1,y),
                    "yp" : lambda x,y: (x,y+1),
                    "ym" : lambda x,y: (x,y-1),
     	}
                
        # run update with correct function

        def updater(x,y):
          return update_switch[chooser[0]](x,y)

        (x,y) = updater(x,y)

        #print("after",x,y) # test that updater is working as planned

        t = t + twait
   
        tout.append(t)
        xout.append(x)
        yout.append(y)
    
    
    return xout,yout,tout



################   Main prog      ###########################################

if __name__ == "__main__":

    t = np.linspace(0, 10,  2000)     
    X0 = np.array([10, 5])      # initials conditions: 10 prey and 5 predators, also pinched off web 
    seed = 1
    a = 1.   
    b = 0.1  
    c = 1.5  
    d = .075  
    

    X = integrate.odeint(dX_dt, X0, t)

    prey = X[:,0]
    pred = X[:,1]

    lv_plot(prey,pred,t)

    lv_plot_phase(prey,pred)
    
    pred,prey,t = gillespie(X0,t,seed)

    lv_plot(pred,prey,t)

    lv_plot_phase(prey,pred)
 


