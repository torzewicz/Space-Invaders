import pygame
from pygame.math import Vector2

class Ammo(object):

    def __init__(self,game):
        self.game = game
        self.x = 400
        self.y = 10

    def tick(self):
        pass

    def draw(self,ammo):

        self.ammo = ammo
        myfont = pygame.font.SysFont("monospace",50)
        label = myfont.render("AMMO:", 1, (255,255,255))
        self.game.screen.blit(label,(self.x , self.y))
        score_n = myfont.render(str(self.ammo),1,(255,255,255))
        self.game.screen.blit(score_n,(self.x + 150, self.y))
