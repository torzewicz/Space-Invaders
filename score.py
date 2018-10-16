import pygame
from pygame.math import Vector2

class Score(object):

    def __init__(self,game):
        self.game = game
        self.x = 10
        self.y = 10

    def tick(self):
        pass

    def draw(self,score):

        self.score = score
        myfont = pygame.font.SysFont("monospace",50)
        label = myfont.render("SCORE:", 1, (255,255,255))
        self.game.screen.blit(label,(self.x , self.y))
        score_n = myfont.render(str(self.score),1,(255,255,255))
        self.game.screen.blit(score_n,(self.x + 178, self.y))
