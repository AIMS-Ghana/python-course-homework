#!/usr/bin/python
from math import pi

def circle(a):
    return (a/pi)**0.5

def square(a):
    return a**0.5


def triangle(a):
    return 2*(a/(3**0.5))**0.5

shaper = {
  'CIRCLE': circle,
  'TRIANGLE': triangle,
  'SQUARE': square
}

output_mods = {
    'TRIANGLE':'equilateral '
}

dim_name = {
    'CIRCLE':'radius'
}

def compute(shape, a):
    assert shape in shaper, "Shape "+shape+" not parseable"
    return shaper[shape](a)

import sys

if __name__ == "__main__":
    assert len(sys.argv) == 3, "need SHAPE, area as argv"
    shape = sys.argv[1]
    area = float(sys.argv[2])
    out = "{}{}, area {}, {}: {} "
    print(out.format(
      output_mods.get(shape,''),
      shape,
      area,
      dim_name.get(shape,'side'),
      compute(shape, area)
    ))
