import pygame
from pygame.math import Vector2

class Pause(object):

    def __init__(self,game):
        self.game = game
        self.x = self.game.SCREEN_SIZE[0]/2 - 360
        self.y = self.game.SCREEN_SIZE[1]/2 - 200

    def tick(self):
        pass

    def draw(self):

        myfont = pygame.font.SysFont("monospace",200)
        label = myfont.render("PAUSE", 1, (255,0,255))
        self.game.screen.blit(label,(self.x+50 , self.y))