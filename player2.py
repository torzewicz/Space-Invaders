import pygame
from pygame.math import Vector2


class Player2(object):

    def __init__(self,game):
        self.game = game
        self.speed = 1.75
        self.r = 2.0
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.tps_max = 300.0
        self.i = 0

        size = self.game.screen.get_size()

        self.pos = Vector2(size[0]/2,size[1]-25)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)

    def add_force(self,force):
        self.acc += force

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a] and self.pos[0]>5:
            self.add_force(Vector2(-self.speed,0))
        if pressed[pygame.K_d] and self.pos[0]<self.game.SCREEN_SIZE[0]-50:
            self.add_force(Vector2(self.speed,0))


        # Fizyka
        self.vel *= 0.4

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        self.tps_delta += self.tps_clock.tick() / 1000.0
        img_names = ["player2.png"]

        self.game.screen.blit(pygame.image.load(img_names[self.i]), self.pos)
        if self.tps_delta >= 75 / self.tps_max:
            self.tps_delta = 0
            self.i += 1
        if self.i > 0:
            self.i = 0





