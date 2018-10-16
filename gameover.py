import pygame
from pygame.math import Vector2

class GameOver(object):

    def __init__(self,game):
        self.game = game
        self.x = self.game.SCREEN_SIZE[0]/2 -350
        self.y = self.game.SCREEN_SIZE[1]/2 - 200

    def tick(self):
        pass

    def draw(self):

        myfont = pygame.font.SysFont("monospace",100)
        label = myfont.render("GAME OVER", 1, (255,0,255))
        self.game.screen.blit(label,(self.x+50 , self.y))
        label2 = myfont.render("PRESS ENTER",1,(255,0,255))
        self.game.screen.blit(label2,(self.x, self.y+150))
