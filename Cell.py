

class Cell:
    def __init__(self, y, x, north=1, east=1, south=1, west=1, occupied=None):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.x = x
        self.y = y
        self.occupied = occupied  # None for free, or the Node that occupies it
        self.neighbours = []  # A list of neighbours to which an edge exists

