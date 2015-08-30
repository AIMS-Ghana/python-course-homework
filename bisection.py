def b_root(a, b):
        return a * b > 0
def bisect(func, v, w):
    'Find root of continuous function where f(v) and f(w) have opposite signs'

    assert not b_root(func(v), func(w))

    for i in range(0, 20):
        midpoint = (v + w) / 2.0
        if b_root(func(v), func(midpoint)):
            v = midpoint
        else:
            w = midpoint

    return midpoint

def f(x):
        return -26 + 85*x - 91*x**2 +44*x**3 -8*x**4 + x**5

x = bisect(f, 0, 1)
print (x, f(x))

