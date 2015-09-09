#!/usr/bin/env/ python3

''' Numerical simulation of an SEIR model using an ODE solver and the Gillespie algorithm '''


def check_config(config):
    ''' Inspects the given configuration file for correctness. '''
    pass


import numpy as np
from scipy.integrate import odeint
def ode_solve(config):
    ''' Solve the ordinary differental equation of the SEIR model. Return [numerical] graph of solutions'''
    pass

# Main program flow
if __name__ == '__main__':
    import sys
    input_file = sys.argv[1]
    config = json.load(open(input_file)) # config is a dictionary that is keyed by the required parameters.
    check_config(config) # inspect the configuration for appropriateness
    pass