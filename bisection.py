#!/usr/bin/python



#bisection function
def root(f, rangex,tol=1.0e-5):

	point_a = rangex[0]
	point_b = rangex[1]

	mid_point = float((point_a+point_b)/2)
        max_err = (point_b-point_a)/2
	while max_err > tol:
		if f(mid_point) == 0:
			break
		elif f(point_a)*f(mid_point) < 0:
			point_b = mid_point
		else:
			point_a = mid_point
		# new estimate
		mid_point = float((point_a+point_b)/2)
		max_err =float( (point_b-point_a)/2)
	return max_err




def root_old(function,rangex,error_tolerance=1.0e-4):
    fu=function(rangex[1])
    if fu==0.0 :  return rangex[1]
    fl=function(rangex[0])
    if fl==0.0 :  return rangex[0]
    if fu*fl > 0.0:  #if the product of the function values at the two bounds is positive, then they do not bracket a root
        return None
    else:
        mid=(rangex[0]+rangex[1])/2
        error=(rangex[1]-rangex[0])/2
        while(error>error_tolerance): #the loop executes till the desired level of accuracy is attainedfm=function(mid)
            fu=function(rangex[1])
            fl=function(rangex[0])

            #if the middle value is indeed the root, it is returned as the root
            if fm==0.0 : return mid

            #if the actual root lies between upper bound and the middle value, the lower bound is set to be the middle value
            elif fu*fm < 0.0 : rangex[0]=mid

            ##if the actual root lies between lower bound and the middle value, the upper bound is set to be the middle value
            elif fl*fm < 0.0 : rangex[1]=mid
            
            mid=(rangex[0]+rangex[1])/2
            error=(rangex[1]-rangex[0])/2
        return mid



