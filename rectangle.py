import math,sys
area=" "
perimeter=" "
value= "Area={0}\nPerimeter={1}"
p=math.pi
def area(l,w):
	
	area_value=float 
	area_value=l*w
	return area_value
def perimeter(l,w):
	perimeter_value=float
	perimeter_value=2*(l+w)
	return perimeter_value

if __name__ == "__main__": 
	if (len(sys.argv))>(3):
	  print ("Wrong input")
	  area="not vaild"
	  perimeter="not vaild"
	elif (len(sys.argv))==(3) :
	  w=float(sys.argv[1])
	  l=float(sys.argv[2])
	  b=perimeter(w,l)
	  c=area(w,l)
	  print (value.format(c,b))
	else:
	  w=float(sys.argv[1])
	  l=float(sys.argv[1])
	  b=perimeter(w,l)
	  c=area(w,l)

	  print (value.format(c,b))

