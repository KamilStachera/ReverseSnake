class Coords:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def isEqual(self, z):
        if self.x == z.x and self.y == z.y:
            return 1
        else:
            return 0
