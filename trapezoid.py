#!/usr/bin/python

def integrate(f, rangex):
    for i in range(len(rangex)-1):
        h = (rangex[i+1] - rangex[i])/2
        m = (f(rangex[i-1]) + f(rangex[i]))
     
        result = 0
    result = result + h*m
    return result

if __name__ == "__main__":
    print(integrate(lambda x:x, thing))
