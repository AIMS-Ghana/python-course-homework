import sys
area= " "
perimeter = " "
greeting="area={0} \n perimeter={1}"
a=sys.argv[1]
b=sys.argv[2]
c=sys.argv[3]
f= 1.73/4 *int(a)
h=(int(a)+int(b)+int(c))

area= str(f)
perimeter= str(h)
print(greeting.format(area,perimeter))
