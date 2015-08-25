import sys
area= " "
perimeter = " "
greeting="area={0} \n perimeter={1}"
a=sys.argv[1]
f=(int(a)*int(a)* 3.14)
h=(2 * int(a) * 3.14)

area= str(f)
perimeter= str(h)
print(greeting.format(area,perimeter))
