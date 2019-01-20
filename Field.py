from Coords import Coords


class Field:
    def __init__(self, x, y, type):
        self.coords = Coords()
        self.coords.x = x
        self.coords.y = y
        self.type = type
