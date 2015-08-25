#!/usr/local/bin/python3

from math import pi

def circle(a:float) -> float:
    return (a/pi)**0.5

def square(a:float) -> float:
    return a**0.5

# heron's rule: area = sqrt(p(p-a)(p-b)(p-c))
# p = (a+b+c)/2
# for eq.tri, a=b=c => p = 3a/2
# area = sqrt(3*(a/2)^4) = sqrt(3)*(a^2)/4
def triangle(a:float) -> float:
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

def compute(shape:str, a:float) -> float:
    assert shape in shaper, "Shape "+shape+" not parseable"
    return shaper[shape](a)

import sys

if __name__ == "__main__":
    assert len(sys.argv) == 3, "need SHAPE, area as args"
    shape = sys.argv[1]
    area = float(sys.argv[2])
    out = "{}{}, area {}, {}: {}"
    print(out.format(
      output_mods.get(shape,''),
      shape,
      area,
      dim_name.get(shape,'side'),
      compute(shape, area)
    ))
