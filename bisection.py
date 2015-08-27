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