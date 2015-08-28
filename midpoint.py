#!/usr/bin/python

def integrate(f,p):
    kof = 0
    for i in range(len(p)-1):
        w = p[i+1] - p[i]
        h = f((p[i+1] + p[i])/2)
        kof = kof + w*h
    return kof



   

#if __name__ == "__main__":
#print(integrate(lambda x:x, thing))

 #main(sys.argv[2:])
