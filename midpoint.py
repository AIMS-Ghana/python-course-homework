#!/usr/bin/python

def integrate(f, rangex):
    for i in range(len(rangex)-1):
        h = rangex[i+1] - rangex[i]
        m = f((rangex[i]+rangex[i+1])/2)
        result = 0
    
    result = result + h*m
    return result

if __name__ == "__main__":
    print(integrate(lambda x:x, thing))
