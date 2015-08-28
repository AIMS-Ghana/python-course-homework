#!/usr/bin/python


def integrate(f, rangex):
	sum=0
        for i in  range (len(rangex) - 1):
        	w=rangex[i+1]-rangex[i]
	    	h=f((rangex[i+1]+rangex[i])/2)
        return sum

 #       if__name__=="__main__":
 # #	main(sys.argv(1)




