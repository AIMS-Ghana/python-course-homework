
#!/usr/bin/python 
import sys 
##if len(sys.argv)== 3 
##     print(sys.argv[1] * sys.argv[2] 
l = float(sys.argv[1]) 
w = float(sys.argv[2]) 
h = float(sys.argv[3]) 

assert (l>0) & (w>0) ,"dimension is negative" 
if l > 0 : 
  print ("negative") 
elif w,0: 
  print ("error") 
else: 
  area = (l*h)/2 
  perimeter=l+h+w 
  print("area is equal", area) 
  print("perimeter is equal to", perimeter) 



