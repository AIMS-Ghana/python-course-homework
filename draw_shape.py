#!/usr/bin/python
#draw shapes of circle, equilateral triangle and square
import sys
import turtle
import shapes
import math
def draw_triangle(side):
	shape = turtle.Screen()
	window=turtle.Turtle()
	window.foward(side)
	window.left(120)
	turtle.foward(side)
	turtle.left(120)
	turtle.foward(side)
	turtle.left(120)
	shape.exitonclick()
draw_triangle(side)
def draw_square(width):
	shape = turtle.Screen()
	turtle.foward(width)
	turtle.left(90)
	turtle.foward(width)
	turtle.left(90)
	turtle.foward(width
	turtle.left(90)
	shape.exitonclick()
draw_square(width)
def draw_circle():	
	begin_fill()
while True:
    forward("CIRCLE")
    left(1)
    if abs(pos()) < 1:
        break
end_fill()
done()
draw_circle(radius)
def main():
	draw_triangle(side)
	draw_square(width)
	draw_circle(radius)
if __name__=="__main__":
	main()
#!/usr/bin/python
#draw shapes of circle, equilateral triangle and square
import sys
import turtle
import shapes
import math
def draw_triangle(side):
    window = turtle.Screen()
  
    turtle.forward(side) 
    turtle.color('blue')
    turtle.left(120)
    turtle.forward(side)
    turtle.color('blue')
    turtle.left(120)
    turtle.forward(side)
    window.exitonclick()

def draw_square(width):
    win = turtle.Screen()
    turtle.left(90)
    turtle.forward(width)
    turtle.color('green')
    turtle.left(90)
    turtle.forward(width)
    turtle.color('green')
    turtle.left(90)
    turtle.forward(width)
    turtle.color('green')
    turtle.left(90)
    turtle.forward(width)
    turtle.color('green')
    turtle.left(90)
    win.exitonclick() #to exit

def draw_circle(rad):	
	window = turtle.Screen()
	circle_drw = turtle.Turtle()
	circle_drw.speed(20)
        circle_drw.circle(rad)
	window.exitonclick() 

	

if __name__=="__main__":
	draw_triangle(100)
	draw_square(100)
	draw_circle(100)
