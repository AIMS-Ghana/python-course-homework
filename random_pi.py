#!/usr/bin/python3
# This program estimates the value of pi using random number generation

# Included below is the expected program output
# $ ./random_pi.py 0 10000
# circle-area pi: ...
# sphere-volume pi


import random
# Usage random.uniform(0,1)


# Here is implemented a method based on the area of a quater of a circle in a square
def circle_area(seed, size):
    random.seed(seed)
    tally = 0
    for i in range(size):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if x**2 < 1 - y**2:
            tally += 1
    return 4 * tally/size


# Here is implemented a method based on the volume of an eigth of a ball in a cube
def sphere_volume(seed, size):
    random.seed(seed)
    tally = 0
    for i in range(size):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        z = random.uniform(0,1)
        if x**2 < 1 - y**2 - z**2:
            tally += 1
    return 3/4 * tally/size * 8


if __name__ == "__main__":
    import sys
    from math import pi
    seed = float(sys.argv[1])
    size = int(sys.argv[2])

    print("circle-area pi: {0}".format(circle_area(seed,size)))
    print("sphere-volume pi: {0}".format(sphere_volume(seed,size)))
    print("correct value of pi: {0}".format(pi))