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

   #if __name__ == "__main__":
    #main(sys.argv(1)) # first midpoint
    						# while(condition)loop: means repeat the condition over & over until it is satisfied
       						# for loop: use it when you have a no. of elements that u r going to use over and over
       						# e.g for i in range(5)
						#put here any python code like, while()

    
