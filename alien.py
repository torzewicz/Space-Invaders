import pygame
from pygame.math import Vector2

class Alien(object):

    def __init__(self,game,x,y,add):
        self.game = game
        self.speed = 0.15
        self.x = x
        self.y = y
        self.add = add

        self.toDestroy = False

    def move(self):
        self.x += self.speed + 0.02 * self.add

    def shiftDown(self):
        self.speed *= -1
        self.y += 20

    def destroy(self):
        self.toDestroy = True

    def draw(self):
        alien = pygame.image.load("ship.png")
        self.game.screen.blit(alien,(self.x,self.y))