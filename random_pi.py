#!/usr/bin/python3
# This program estimates the value of pi using random number generation

#Included below is the expected program output
#$ ./random_pi.py 0 10000
#circle-area pi: ...
#sphere-volume pi


import random
#Usage random.uniform(0,1)
import numpy



#Here we receive a sample of coordinates on a square and determine the weight of points in a quarter-circle region
def circle_area(sqsample):
    total = len(sqsample)
    tally = 0
    for i in range(total):
        if (sqsample[i][0])**2  < 1 - (sqsample[i][1])**2:
            tally += 1
    return 4 * tally/total


#Here we receive a sample of coordinates in a cube and determine the weight of points in a ball
def sphere_volume(cbsample):
    total = len(cbsample)
    tally = 0
    for i in range(total):
        if (cbsample[i][0] )**2 < 1 - (cbsample[i][1] )**2 - (cbsample[i][2] )**2:
            tally += 1
    return (3/4 * tally/total * 8)

def square(seed, size):
    board = numpy.zeros([size,2])
    for i in range(size):
        board[i][0] = random.uniform(0,1)
        board[i][1] = random.uniform(0,1)
    return board

def ball(seed, size):
    board = numpy.zeros([size,3])
    for i in range(size):
        board[i][0] = random.uniform(0,1)
        board[i][1] = random.uniform(0,1)
        board[i][2] = random.uniform(0,1)
    return board


if __name__ == "__main__":
    import sys
    from math import pi
    seed = float(sys.argv[1])
    size = int(sys.argv[2])
    print("circle-area pi: {0}".format(circle_area(square(seed,size))))
    print("sphere-volume pi: {0}".format(sphere_volume(ball(seed,size))))
    print("correct value of pi: {0}".format(pi))