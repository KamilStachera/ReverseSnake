from Coords import Coords


class CialoWensza:
    def __init__(self, x, y):
        self.coords = Coords(x, y)

    def prev(self, anc):
        self.anc = anc

    def next(self, nxt):
        self.nxt = nxt
