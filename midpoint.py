 #!/usr/bin/python

 def f(x):
    return 0.5 + x*x

def midpoint(u, v, f, nbins=10):

    h = float(u-v)/nbins
    assert h > 0
    assert type(nbins) == int
    
    sum = 0.0
    x = u + h/2
     while (x < v):
         sum += h* f(x)
         x += h

    return sum


