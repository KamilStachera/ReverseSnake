import pygame, sys
import thorpy
import time
from Coords import Coords


class Display:
    def __init__(self, world, fields):
        pygame.init()
        self.wall = pygame.image.load("Graphics/wall.png")
        self.grass = pygame.image.load("Graphics/trawa.png")
        self.snake = pygame.image.load("Graphics/wonsz.png")
        self.strawberry = pygame.image.load("Graphics/malinka.png")
        self.world = world
        self.fields = fields
        self.screen = pygame.display.set_mode((self.world.x * 40, self.world.y * 40))
        self.mainGameLoop()

    def mainGameLoop(self):
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.world.changeDirection("N")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.world.changeDirection("S")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.world.changeDirection("W")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.world.changeDirection("E")
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("lol")

            self.world.executeTurn()
            self.draw()
            time.sleep(0.2)

    def draw(self):
        for field in self.fields:
            if field.type == "W":
                self.screen.blit(self.wall, (field.coords.x * 40, field.coords.y * 40))
            if field.type == "B":
                self.screen.blit(self.snake, (field.coords.x * 40, field.coords.y * 40))
            if field.type == "Z":
                self.screen.blit(self.grass, (field.coords.x * 40, field.coords.y * 40))
            if field.type == "M":
                self.screen.blit(self.strawberry, (field.coords.x * 40, field.coords.y * 40))
        pygame.display.flip()
