import turtle
import shapes

def draw(shape,area,fill="black",cont="False"):
 turtle.ht ()
 if shape=="CIRCLE":
	r=shapes.calcir(area)
	turtle.begin_fill()
	turtle.color(fill)
	turtle.circle(r)
	turtle.home ()
	turtle.end_fill()
	
 if shape=="SQUARE":
	l=shapes.calsqr(area)
        turtle.begin_fill()
	turtle.color(fill)
	turtle.left(90)
	turtle.forward(l)
	turtle.left(90)
	turtle.forward(l)
	turtle.left(90)
	turtle.forward(l)
	turtle.left(90)
	turtle.forward(l)
	turtle.home ()
	turtle.end_fill()
	
 if shape=="TRIANGLE":
	l=shapes.caltrin(area)
	turtle.begin_fill()
	turtle.color(fill)
	turtle.forward(l) 
	turtle.left(120)
	turtle.forward(l)
	turtle.left(120)
	turtle.forward(l)
	turtle.home ()
	turtle.end_fill()
 if not cont:
	turtle.existonclick()

	

 #turtle.exitonclick()

if __name__ == "__main__": 
	
  shape=str(sys.argv[1])
	 
  area=float(sys.argv[2])
  draw(shape,area)
	

