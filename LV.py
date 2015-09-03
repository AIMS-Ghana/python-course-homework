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


#################   plot         #####################################

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

        twait = npr.exponential(1/L)

        prob_xp = a*x/L
        prob_xm = b*x*y/L
        prob_yp = d*x*y/L
        prob_ym = c*y/L
    

        p =[prob_xp, prob_xm, prob_yp, prob_ym]

        #print("before",x,y)
        
        chooser =  npr.choice(["xp","xm","yp","ym"],1,p=p)
       
       

        update_switch ={
                    "xp" : lambda x,y: (x+1,y),
                    "xm" : lambda x,y: (x-1,y),
                    "yp" : lambda x,y: (x,y+1),
                    "ym" : lambda x,y: (x,y-1),
     	}
        
        def updater(x,y):
          return update_switch[chooser[0]](x,y)

        (x,y) = updater(x,y)

        #print("after",x,y) 

        t = t + twait
   
        tout.append(t)
        xout.append(x)
        yout.append(y)
    
    
    return xout,yout,tout



################   Main prog      ###########################################

if __name__ == "__main__":

    t = np.linspace(0, 10,  1000)     
    X0 = np.array([10, 5])      # initials conditions: 10 prey and 5 predators, also pinched off web 
    seed = 1
    a = 1.   
    b = 0.1  
    c = 1.5  
    d = .075  
    zed = 0

    X = integrate.odeint(dX_dt, X0, t)

    prey = X[:,0]
    pred = X[:,1]

    lv_plot(prey,pred,t)
    
    xout,yout,tout = gillespie(X0,t,seed)

    lv_plot(xout,yout,tout)
 


