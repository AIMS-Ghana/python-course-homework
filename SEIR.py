#!/usr/bin/python3

''' Numerical simulation of an SEIR model using an ODE solver and the Gillespie algorithm '''


def check_config(config):
    ''' Inspects the given configuration file for correctness. '''
    pass


import numpy as np
from scipy.integrate import odeint
import  matplotlib.pyplot as pyplot


def ode_solve():
    ''' Solve the ordinary differental equation of the SEIR model. Return [numerical] graph of solutions '''
    t = np.linspace(0, tmax, 1000)
    states = odeint(equations, Y0, t)
    return (t, states[:,0],states[:,1],states[:,2],states[:,3])


def equations(state,t):
    s = state[0]
    e = state[1]
    i = state[2]
    r = state[3]

    ds = mu*N - beta*s*i/N - mu*s
    de = beta*s*i/N - sigma*e - mu*e
    di = sigma*e - gamma*i - mu*i
    dr = gamma*i - mu*r
    return [ds,de,di,dr]


def plotter(graphs):
    ''' Generate the diagrramatic plot of the given graphs. '''
    t =  graphs[0]
    s, = pyplot.plot(t,graphs[1],'r')
    e, = pyplot.plot(t,graphs[2],'b')
    i, = pyplot.plot(t,graphs[3],'y')
    r, = pyplot.plot(t,graphs[4],'g')
    pyplot.legend([s, e, i,r],['S','E','I','R'])



def gpe(n, file = False):
    ''' A single run of the Gillespie algorithm using global configuration parameters. Return [numerical] graph of a run'''
    # send a state to what_next and get the next iteration back
    T, S, E, I, R = [],[],[],[],[]
    t = 0
    state = Y0
    while t < tmax:
        if state[0] != N:
        #print(state)
            output(t,state[0],state[1],state[2],state[3], file, n)
            T.append(t)
            S.append(state[0])
            E.append(state[1])
            I.append(state[2])
            R.append(state[3])
            next = what_next(state)
            t += next[0]
            state = next[1]
        else:
            break
    return (T,S,E,I,R)


possibs = {    1:[-1,1,0,0],
               2:[0,-1,1,0],
               3:[0,0,-1,1],
               4:[1,-1,0,0],
               5:[1,0,-1,0],
               6:[1,0,0,-1]
           }


def what_next(state): #state state should be a numpy array
    ''' One choice of gpe '''
    probs = np.array([beta * state[0]* state[2] / N,
                      sigma* state[1],
                      gamma* state[2],
                      mu* state[1],
                      mu* state[2],
                      mu* state[3]])
    rate = sum(probs)
    probs = probs / sum(probs)
    #probs[5] += (1 - sum(probs))
    return np.random.exponential(1/rate), state + possibs[np.random.choice([1,2,3,4,5,6], p = probs)]
    #return np.random.exponential(1/rate), state + possibs[np.random.choice([1,2,3,4,5,6])]


def output(t,s,e,i,r,file, n):
    ''' Write outputs to terminal or to file, as required '''
    if n != 1:
        if file:
            #write.writerow(str_format.format(n,t,s,e,i,r))
            write.writerow([n,t,s,e,i,r])
        else:
            #print(str_format.format(n,t,s,e,i,r))
            print(n,t,s,e,i,r)
    else:
        if file:
            #write.writerow(str_format.format(n,t,s,e,i,r))
            write.writerow([t,s,e,i,r])
        else:
            #print(str_format.format(n,t,s,e,i,r))
            print(t,s,e,i,r)




def check_config(config):
    ''' Check the validity of the input configuration file    '''
    pass


# Main program flow
if __name__ == '__main__':
    import sys
    import csv
    import json

    input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
        csvfile = open(output_file,'w')
        write = csv.writer(csvfile)
    if len(sys.argv) > 3:
        output_image = sys.argv[3]
  
   

    config = json.load(open(input_file)) # config is a dictionary that is keyed by the required parameters.
    check_config(config) # inspect the configuration for appropriateness
    beta, sigma, mu, gamma, Y0, tmax = config['beta'], config['sigma'],config['mu'],config['gamma'], np.array(config['Y0']), config['tmax']
    N = sum(Y0)
    n = 100

    if n == 1 and len(sys.argv) > 2:
        write.writerow(['t','s','e','i','r'])
    elif n!=1 and len(sys.argv) > 2:
        write.writerow(['n','t','s','e','i','r'])

    plotter(ode_solve())
    for i in range(50):
        plotter(gpe(i + 1,file = len(sys.argv) > 2))
    #pyplot.show()
    if len(sys.argv) > 3:
        pyplot.savefig(output_image)
    else:
        pyplot.show()

