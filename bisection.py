#!/usr/bin/python

def root(f, endpoints, tol=1e-5):
    mid = (endpoints[1]+endpoints[0])/2
    midval = f(mid)
    if abs(midval) < tol:
        return mid
    else:
        lowval = f(endpoints[0])
        if lowval < 0:
            if midval < 0:
                low = mid
                high = endpoints[1]
            else:
                low = endpoints[0]
                high = mid
        else:
            if midval > 0:
                low = mid
                high = endpoints[1]
            else:
                low = endpoints[0]
                high = mid
        return root(f, (low,high), tol)
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
 
def root2(f, endpoints, tol=1e-5):
    high = endpoints[1]
    low = endpoints[0]
    mid = (low+high)/2
    midval = f(mid)
    lowval = f(low)
    while (abs(midval) > tol):
        if lowval < 0:
            if midval < 0:
                low = mid
                lowval = midval
            else:
                high = mid
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
            if midval > 0:
                low = mid
                lowval = midval
            else:
                high = mid
        mid = (low+high)/2
        midval = f(mid)
    return mid
            a = m
            fa = fm
        m = (a+b)/2
        fm = f(m)
        depth = depth - 1
    return m 
