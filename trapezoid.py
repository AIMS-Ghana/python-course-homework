#!/usr/bin/env python3

def integrate(f, rangex):
    riemann_sum = 0
    for i in range(len(rangex)- 1 ):
        riemann_sum += (rangex[i + 1] - rangex[i]) * 0.5 * ( f(rangex[i]) + f(rangex[i+1]) )
    return riemann_sum