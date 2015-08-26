<<<<<<< HEAD
 #!/usr/bin/python3
import sys
##if len(sys.argv)== 2
##	print(sys.argv[1]* sys.argv[2] 
l=float(sys.argv[1]) 
w=float(sys.argv[2])
assert (l>0) & (w>0); "a dimension is negative"
if l< 0 :
 print("negative length")
elif w< 0 :
 print("error")
else :
 area= l*w
 perimeter=2*(l+w)
 print("area is equal to",area)
 print("perimeter is equal to",perimeter)


=======
#!/usr/bin/env python3






def check(a,b):
	assert (a>0) & (b>0)  ,"inserted negative integers"
	

def area(a:float,b:float):
	check(a,b)
	res=a*b
	return res


def perimeter(a,b):
	check(a,b)
	rest=(a+b)*2
	return rest

import sys

if __name__=="__main__":
	a=float(sys.argv[1])
	b=float(sys.argv[2])
	print ("area {},perimeter {}".format(area(a,b), perimeter(a,b)))

	
>>>>>>> origin/master
