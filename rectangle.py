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


