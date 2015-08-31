import turtle
import shapes

def draw(shape,area):
 turtle.ht ()
 if shape=="CIRCLE":
	r=shapes.calcir(area)
	turtle.circle(r)
	turtle.home ()

 if shape=="SQUARE":
	l=shapes.calsqr(area)
	turtle.left(90)
	turtle.forward(l)
	turtle.left(90)
	turtle.forward(l)
	turtle.left(90)
	turtle.forward(l)
	turtle.left(90)
	turtle.forward(l)
	turtle.home ()

 if shape=="TRIANGLE":
	l=shapes.caltrin(area)
	turtle.forward(l) 
	turtle.left(120)
	turtle.forward(l)
	turtle.left(120)
	turtle.forward(l)
	turtle.home ()
	

 turtle.exitonclick()

if __name__ == "__main__": 
	
  shape=str(sys.argv[1])
	 
  area=float(sys.argv[2])
  draw(shape,area)
	

