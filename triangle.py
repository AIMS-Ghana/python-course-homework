import math,sys
area=" "
perimeter=" "
value= "Area={0}\nPerimeter={1}"
def check(a,b,c):
	su=a+b
	d=a-b
	assert ((a>0) & (b>0) & (c>0)),"negative value"
	assert ((su>c) & (d<c)),"not vaild"
	

def perimeter(a,b,c):
	check(a,b,c)
	perimeter_value=a+b+c
	#print (perimeter_value)
	return perimeter_value

def area(a,b,c):
	check(a,b,c)
	s1= perimeter(a,b,c)
	s=s1*.5
	sa=s-a
        sb=s-b
	sc=s-c
	ss=s*sa*sb*sc
	area_value=math.sqrt(ss)
	return area_value

if __name__ == "__main__": 
	if (len(sys.argv))>(4):
	  print ("Wrong input")
	  area="not vaild"
	  perimeter="not vaild"
	
	else:
	  a=float(sys.argv[1])
	  b=float(sys.argv[2])
	  c=float(sys.argv[3])
	  p=perimeter(a,b,c)
	  ar=area(a,b,c)

	  print (value.format(ar,p))

