#!/usr/bin/python

def integrate(f, rangex):
    ss = 0
    for i in range(len(rangex)-1):
        a = rangex[i]
        b = rangex[i+1]
        w = b - a
        fa = f(a)
        fb = f(b)
        ss = ss + w*(fa+fb)/2
    return ss
    # get range widths
    # get range midpoints

if __name__ == "__main__":

    print(integrate(lambda x:x, thing))
