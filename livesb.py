import pygame
from pygame.math import Vector2

class Livesb(object):

    def __init__(self,game):
        self.game = game
        self.x = 840
        self.y = 10

    def tick(self):
        pass

    def draw(self, lives):

        self.lives = lives
        myfont = pygame.font.SysFont("monospace",50)
        label = myfont.render("LIVES:", 1, (255,255,255))
        self.game.screen.blit(label,(self.x, self.y))

        for i in range(0,self.lives):
            self.game.screen.blit(pygame.image.load("player_b.png"), (self.x+200+i*75,self.y+10))
