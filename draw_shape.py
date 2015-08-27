#!/use/bin/env python
from tkinter import *
from random import *

class Application(Canvas):

    X_OFFSET = 40
    Y_OFFSET = 40
    FILL = 'blue'
    LINE = 'black'

    @classmethod
    def main(cls):
        root = Tk()
        surface = cls(root)
        surface.grid()
        surface.after_idle(surface.draw_shape)
        root.mainloop()

    def draw_shape(self):
        x = randrange(int(self['width']) - self.X_OFFSET)
        y = randrange(int(self['height']) - self.Y_OFFSET)
        points = [(x + randrange(self.X_OFFSET), y + randrange(self.Y_OFFSET))
                  for point in range(randint(3, 10))]
        self.create_polygon(points, fill=self.FILL, outline=self.LINE)
        self.after(1000, self.draw_shape)

if __name__ == '__main__':
    Application.main()
