#!/usr/bin/python
 
def integrate(f, rangex):
    ss = 0
    for i in range(len(rangex)-1):
        w = rangex[i+1] - rangex[i]
        h = f((rangex[i+1] + rangex[i])/2)
        ss = ss + w*h
    return ss
    # get range widths
    # get range midpoints

if __name__ == "__main__":
    print(integrate(lambda x:x, thing))
