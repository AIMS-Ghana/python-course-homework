from pylab import *
import curves

v_exp_decay = np.vectorize(curves.exp_decay) # exponential decay, rate 1
v_exp_saturation = np.vectorize(curves.exp_saturation) # exponential saturation, rate 1
v_line = np.vectorize(curves.line) # line, slope 2, y-intercept 2

def plotting(start, end):
    X = np.linspace(start, end)
    D = v_exp_decay(X)
    S = v_exp_saturation(X)
    L = v_line(X)
    plot(X, E, '-r', label="Decay")
    plot(X, S, ':b', label="Saturation")
    plot(X, L, '.y', label="Line")
    xlabel('x')
    ylabel('y')
    title('Some Curves')
    legend(loc='upper right')
    show()
