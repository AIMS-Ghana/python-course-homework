<<<<<<< HEAD
#!/usr/bin/python
=======
#!/usr/bin/env python3

>>>>>>> origin/master
import numpy as np

import midpoint


def intf(x):
    return np.exp(x)

rangex = np.linspace(0, 10, 100, endpoint=True)

out = "{} integration, e^x on ({},{}): {}"

print(out.format(
    "bisection",
    rangex[-1], rangex[0],
    midpoint.integrate(intf, rangex)
))

from scipy.integrate import quad

print(out.format(
    "scipy",
      rangex[0], rangex[-1],
    quad(intf, rangex[0], rangex[-1])
))

