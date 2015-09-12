def root(f, endpoints, tol=1e-5, depth=100):
    a, b = endpoints
    fa = f(a)
    fb = f(b)
    assert fa*fb < 0, "endpoints have same sign"
    m = (a+b)/2
    fm = f(m)
    if (abs(fm) < tol) or (depth == 0):
        return m
    elif fa*fm < 0: # root in a,m
        return root(f,[a,m],tol,depth-1)
    else: # root in m, b
        return root(f,[m,b],tol,depth-1)

def root2(f, endpoints, tol=1e-5, depth=100):
    a, b = endpoints
    fa = f(a)
    fb = f(b)
    assert fa*fb < 0, "endpoints have same sign"
    m = (a+b)/2
    fm = f(m)
    while (abs(fm) > tol) or (depth != 0):
        if fa*fm < 0:
            b = m
        else:
            a = m
            fa = fm
        m = (a+b)/2
        fm = f(m)
        depth = depth - 1
    return m
