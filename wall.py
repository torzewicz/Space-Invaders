import pygame
from pygame.math import Vector2

class Wall(object):

    def __init__(self,game,x):
        self.game = game
        self.x = x
        self.y = 650
        self.state = 2
        self.toDestroy = False

    def tick(self):
        pass

    def destroy(self):
            self.toDestroy = True

    def draw(self):
        wall1 = pygame.image.load("wall.png")
        wall2 = pygame.image.load("wall2.png")
        wall3 = pygame.image.load("wall3.png")
        if(self.state==2):
            self.game.screen.blit(wall1,(self.x,self.y))
        if(self.state==1):
            self.game.screen.blit(wall2,(self.x,self.y))
        if(self.state==0):
            self.game.screen.blit(wall3,(self.x,self.y))