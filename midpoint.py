def integrate(f, rangex):
    d = 0
    for i in range(len(rangex)-1):
        w = rangex[i+1] - rangex[i]
        h = f((rangex[i+1] + rangex[i])/2)
        d = d + w*h
    return d

if __name__ == "__main__":
    print(integrate (x:x, thing))
