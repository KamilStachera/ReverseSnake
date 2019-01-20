from Coords import Coords
from CialoWensza import CialoWensza


class Wensz:
    def __init__(self, x, y):
        self.startingPosY = y
        self.startingPosX = x
        self.head = CialoWensza(x, y)
        self.container = []
        self.container.append(self.head)
        self.fillSnake()

    def fillSnake(self):
        counter = self.startingPosY
        while True:
            newTile = CialoWensza(self.startingPosX, self.startingPosY - 1)
            newTile.next(self.head)
            newTile2 = CialoWensza(self.startingPosX, self.startingPosY - 2)
            newTile.prev(newTile2)
            newTile2.next(newTile)
            newTile2.prev(None)
            self.head.prev(newTile)
            self.head.next(None)
            self.container.append(newTile)
            self.container.append(newTile2)
            break
