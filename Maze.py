from graphics import *

"""
This class represents the graphical representation of the maze layout
"""


class Maze:
    def __init__(self, grid, dim):
        self.grid = grid  # grid denotes the 2d list of Cells {cells identified in the form (y,x)}
        self.dim = dim  # denotes the number of cells, result is an x-by-x rectangle
        self.step = 50  # denotes the cell size in px
        self.lines = None
        
    def build_maze(self):
        lines = []
        for x in range(self.dim):
            pt = x * self.step
            lines.append(Line(Point(pt, 0), Point(pt + self.step, 0)))
            lines.append(Line(Point(pt, self.dim * self.step), Point(pt + self.step, self.dim * self.step)))
            lines.append(Line(Point(0, pt), Point(0, pt + self.step)))
            lines.append(Line(Point(self.dim * self.step, pt), Point(self.dim * self.step, pt + self.step)))

        # NOTE: maze coordinate system is in the form (Y,X)!
        for x in range(self.dim):
            for y in range(self.dim):
                c = self.grid[y][x]
                # point at (x,y) represents top left corner
                X = x * self.step
                Y = y * self.step
                if c.north == 1:
                    lines.append(Line(Point(X, Y), Point(X + self.step, Y)))
                if c.east == 1:
                    lines.append(Line(Point(X + self.step, Y), Point(X + self.step, Y + self.step)))
                if c.south == 1:
                    lines.append(Line(Point(X, Y + self.step), Point(X + self.step, Y + self.step)))
                if c.west == 1:
                    lines.append(Line(Point(X, Y), Point(X, Y + self.step)))
        self.lines = lines
        return lines
