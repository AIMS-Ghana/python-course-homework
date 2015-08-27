import math,sys
area=" "
perimeter=" "
value= "Area={0}\nPerimeter={1}"
p=math.pi
def area(r):
	
	area_value=float 
	area_value=p*math.pow(r,2)
	return area_value
def perimeter(r):
	perimeter_value=float
	perimeter_value=2*p*r
	return perimeter_value

if __name__ == "__main__": 
	if (len(sys.argv))!=(2):
	  print ("Wrong input")
	  area="not vaild"
	  perimeter="not vaild"
	else:
	  a=float(sys.argv[1])
	  b=perimeter(a)
	  c=area(a)
	  print (value.format(c,b))

