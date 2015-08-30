#!/usr/bin/python

def integrate(f, rangex):
    ss = 0
    for n in range(len(rangex)-1):
        w = rangex[n+1] - rangex[n]
        h = f((rangex[n+1] + rangex[n])/2)
        ss = ss + w*h
    return ss

#get range widths
#get range midpoint
#for all of the pairs in xs
#find midpoint
#get width of pair
#calculate f(mid)
#add f(mid)*w to sum

        
if __name__ =="__main__":
    print(integrate(lambda X:x, thing))

