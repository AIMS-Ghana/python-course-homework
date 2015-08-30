#!/usr/bin/env pytho3


import numpy as np
import midpoint

def intf(x):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    return np.exp(x)

rangex = np.linspace(0, 10, 100, endpoint=True)

out = "{} integration, e^x on ({},{}): {}"

print(out.format(
    "midpoint",
    rangex[0], rangex[-1],
    midpoint.integrate(intf, rangex)
))

from scipy.integrate import quad

print(out.format(
    "scipy",
    rangex[0], rangex[-1],
    quad(intf, rangex[0], rangex[-1])
))
=======
	n = float (10) / x
	return n


if __name__ == "__main__":
	rangex = range (100)
	print(midpoint.integrate(intf(100), rangex))

# x = 100
# rangex = range (100)
>>>>>>> Stashed changes
=======
	n = float (10) / x
	return n


=======
	n = float (10) / x
	return n


>>>>>>> Stashed changes
if __name__ == "__main__":
	rangex = range (100)
	print(midpoint.integrate(intf(100), rangex))

# x = 100
# rangex = range (100)
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
