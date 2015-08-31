import matplotlib.pyplot as plt
def fun(f, xs):
    fx= f(xs)
    plt.plot(xs,fx)
    plt.ylabel('some number')
    plt.show()

def H(x):
    return x

fun(H,[0,1,2,3,4])
