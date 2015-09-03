
from numpy import gradient
from scipy.integrate import odeint


def sine_and_cos(t):
    return np.sin(t) + np.cos(t)


def calc_all(h, rangex, ifxmin = 0):
    hx = h(rangex)
    return {
        'h'  : hx,
        'dh' : gradient(hx),
        'Ih' : odeint(lambda y, x:h(x), 0, rangex)s
    }

import matplotlib.pyplot as pyplot

def plot_all(h, rangex, ifxmin = 0):
    lines = calc_all(h, rangex, ifxmin)
    hx, = pyplot.plot(rangex, lines['h'], '-')
    dh, = pyplot.plot(rangex, lines['dh'], ":")
    Ih, = pyplot.plot(rangex, lines['Ih'], "--")
    pyplot.legend([hx, dh, Ih],['function','derivative','integral'])
    pyplot.show()

if __name__ == "__main__":
    from numpy import linspace
    x = linspace(-10,15,25,endpoint=True)
    plot_all(lambda x:x, x)
    plot_all(Ih, x)
    plot_all(Ih, x)
