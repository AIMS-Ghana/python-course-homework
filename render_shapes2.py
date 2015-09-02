#!/usr/bin/python3
from draw_shape import draw

draw("CIRCLE", 1000, cont=True) # draw a black circle, then continue
draw("SQUARE", 6000, "RED", True) # draw a red square, then continue
draw("TRIANGLE", 1000, "GREEN") # draw a green triangle, then done
