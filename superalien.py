import pygame
from pygame.math import Vector2

class SuperAlien(object):

    def __init__(self,game):
        self.game = game
        self.speed = 0.55
        self.x = 1280
        self.y = 54

        self.toDestroy = False

    def move(self):
        self.x -= self.speed


    def destroy(self):
        self.toDestroy = True

    def draw(self):
        alien = pygame.image.load("shipS.png")
        self.game.screen.blit(alien,(self.x,self.y))