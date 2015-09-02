def root(f, interval, tol=1e-5, steps=100):
    b0, b1 = interval
    d = b1 - b0
    f0 = f(b0)
    f1 = f(b1)
    m = f1 - f0
    bn = b1-f1*d/m
    fn = f(bn)
    if (fn <= tol) or (steps == 0):
        return bn
    else:
        return root(f, [b1, bn], tol, steps)
