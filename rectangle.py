import sys
area= " "
perimeter = " "
greeting="area={0} \nperimeter={1}"
a=sys.argv[1]
b=sys.argv[2]

f=int(a)*int(b)
h=2 * (int(a)+int(b))


area= str(f)
perimeter= str(h)
print(greeting.format(area,perimeter))


