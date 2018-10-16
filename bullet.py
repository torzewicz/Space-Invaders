import pygame

from pygame.math import Vector2

import math
class Bullet(object):

    def __init__(self,game,x,y):
        self.game = game
        self.x = x
        self.y = y
        self.speed = 3.0
        self.r = 2
        self.toDestroy = False

    def tick(self):

        self.y -= self.speed

    def hits(self,alien):
        if (self.x >= alien.x and self.x<=alien.x+50 and self.y >= alien.y and self.y <= alien.y+50):
            return True
        else:
            return False

    def hits_wall(self,wall):
        if(self.y<wall.y+50 and self.x>=wall.x and self.x<=wall.x+100):
            return True
        else:
            return False

    def hits_super(self,super):
        if (self.x >= super.x and self.x<=super.x+80 and self.y >= super.y and self.y <= super.y+65):
            return True
        else:
            return False

    def destroy(self):
        self.toDestroy = True


    def draw(self):
        box = (self.x,self.y,self.r*2,self.r*2)
        pygame.draw.ellipse(self.game.screen,(255,100,255),box)