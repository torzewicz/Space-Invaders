import pygame

from pygame.math import Vector2

import math

class AlienBullet(object):

    def __init__(self,game,x,y):
        self.game = game
        self.x = x
        self.y = y
        self.speed = -1.2
        self.r = 2
        self.toDestroy = False

    def tick(self):
        self.y -= self.speed

    def hits(self,player):
        if(self.y >= 700 and self.x>= player.pos[0]-25 and self.x<=player.pos[0]+25):
            return True
        else:
            return False

    def hits_wall(self,wall):
        if(self.y >= wall.y - 50 and self.x >= wall.x - 30 and self.x <= wall.x + 70):
            return True
        else:
            return False

    def destroy(self):
        self.toDestroy = True

    def draw(self):
        box = (self.x+25, self.y+33, self.r, 8*self.r)
        pygame.draw.ellipse(self.game.screen,(255,255,255),box)
