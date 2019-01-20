from Coords import Coords
from Field import Field
from Display import Display
from Wensz import Wensz
import random
import copy


class World:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fields = []
        self.direction = "S"
        self.i = 0
        self.fillFields()

    def nieRandomMalinka(self):
        for field in self.fields:
            if field.coords.x == 12 and field.coords.y == 12:
                self.fields.remove(field)
        self.fields.append(Field(12, 12, "M"))
        self.malinkaX = 12
        self.malinkaY = 12

    def randomMalinka(self):
        randX = random.randint(0, self.x)
        randY = random.randint(0, self.y)
        for field in self.fields:
            if field.coords.x == randX and field.coords.y == randY:
                if field.type == "W":
                    self.randomMalinka()
                    break
                else:
                    for field in self.fields:
                        if field.coords.x == randX and field.coords.y == randY:
                            self.fields.remove(field)
                            break
                    self.fields.append(Field(randX, randY, "M"))
                    break

    def fillFields(self):
        for i in range(0, self.x):
            for j in range(0, self.y):
                if i == 0 or j == 0 or i == self.x - 1 or j == self.y - 1:
                    self.fields.append(Field(i, j, "W"))
                else:
                    self.fields.append(Field(i, j, "Z"))
        self.nieRandomMalinka()
        # self.randomMalinka()
        self.newWonsz = Wensz(self.x / 2, self.y / 2)
        self.snakeTiles()
        Display(self, self.fields)

    def changeDirection(self, direction):
        self.direction = direction

    def snakeTiles(self):
        self.licz = 0
        for field in self.fields:
            if field.type == "B":
                self.licz += 1
        self.licz = 0
        for field in self.fields[:]:
            if field.type == "B":
                self.fields.remove(field)
                self.licz += 1
                pom1 = field.coords.x
                pom2 = field.coords.y
                self.fields.append(Field(pom1, pom2, "Z"))

        for tile in self.newWonsz.container:
            for field in self.fields:
                if field.coords.x == tile.coords.x and field.coords.y == tile.coords.y:
                    self.fields.remove(field)
                    break
            self.fields.append(Field(tile.coords.x, tile.coords.y, "B"))

    def executeTurn(self):
        for tile in reversed(self.newWonsz.container):
            if tile.nxt == None:
                if self.direction == "N":
                    self.checkIfDed(tile.coords.x, tile.coords.y - 1)
                    tile.coords.y -= 1
                elif self.direction == "S":
                    self.checkIfDed(tile.coords.x, tile.coords.y + 1)
                    tile.coords.y += 1
                elif self.direction == "W":
                    self.checkIfDed(tile.coords.x - 1, tile.coords.y)
                    tile.coords.x -= 1
                elif self.direction == "E":
                    self.checkIfDed(tile.coords.x + 1, tile.coords.y)
                    tile.coords.x += 1
                self.checkIfMalinka(tile.coords.x, tile.coords.y)
                continue
            else:
                tile.coords = copy.deepcopy(tile.nxt.coords)

        self.snakeTiles()

    def checkIfMalinka(self, x, y):
        if x == 12 and y == 12:
            print("lul")
        for field in self.fields:
            if field.coords.x == x and field.coords.y == y:
                if field.type == "M":
                    for tile in self.newWonsz.container:
                        if tile.anc == None and tile.nxt == None:
                            exit(0)
                        elif tile.anc == None:
                            tile.nxt.anc = None
                            self.newWonsz.container.remove(tile)
                            self.randomMalinka()
                        # self.newWonsz.container.
                else:
                    break

    def checkIfDed(self, x, y):
        for field in self.fields:
            if field.coords.x == x and field.coords.y == y:
                if field.type == "W":
                    exit(0)
                    break
                else:
                    break
