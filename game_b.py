import sys
from sys import exit

import pygame
from pygame.locals import *

from player import Player
from alien import Alien
from bullet import Bullet
from alienbullet import AlienBullet
from livesb import Livesb
from score import Score
from ammo import Ammo
from wall import Wall
from gameover import GameOver
from nextlevel import NextLevel
from superalien import SuperAlien
from pause import Pause
from player2 import Player2

import random

class Game_b(object):
    def __init__(self,gamestate,score,ammo):
        # Konfuguracja

        random.seed()
        #inicjalizaja
        pygame.init()

        self.SCREEN_SIZE = (1280, 720)  # grafiki dopasowane do tego
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.shot = 0.0
        self.supertime = -2

        self.player = Player(self)
        self.player2 = Player2(self)
        self.aliens = []
        self.opp = 10
        self.bullets = []
        self.alienbulets = []
        self.lives = Livesb(self)
        self.lives_number = 3
        self.score = Score(self)
        self.score_number = 0 + score
        self.ammo = Ammo(self)
        self.walls = []
        self.gameover = GameOver(self)
        self.gamestate = gamestate
        self.ammo_number = ammo + 5
        self.nextlevel = NextLevel(self)
        self.tps_max = 300.0
        self.superalien = []
        self.tooClose = False
        self.pauseSign = Pause(self)
        self.pause = 1

        for i in range(0,self.opp):
            self.aliens.append(Alien(self, i * 100 + 100, 100,self.gamestate-1))
            self.aliens.append(Alien(self, i * 100 + 100, 150,self.gamestate-1))
            self.aliens.append(Alien(self, i * 100 + 100, 200,self.gamestate-1))
            self.aliens.append(Alien(self, i * 100 + 100, 250,self.gamestate-1))
            self.aliens.append(Alien(self, i * 100 + 100, 300,self.gamestate-1))
            self.aliens.append(Alien(self, i * 100 + 100, 350,self.gamestate-1))

        self.rand_opp = 6*self.opp

        for i in range(0,5):
            self.walls.append(Wall(self,80+i*340))

        channel_game = pygame.mixer.Channel(1)
        channel_game2 = pygame.mixer.Channel(2)
        channel_game3 = pygame.mixer.Channel(3)

        self.background = pygame.image.load("tlo3.jpg")

        while self.gamestate !=0:

            if self.rand_opp != 0:
                los = random.randrange(self.rand_opp)
            else:
                los = 0
            # obsługa zdarzen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    self.pause *= -1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.ammo_number != 0:
                    self.bullets.append(Bullet(self,self.player.pos[0]+23,self.player.pos[1]))
                    channel_game3.play(pygame.mixer.Sound("mygun.wav"))
                    channel_game3.set_volume(0.5)
                elif (self.lives_number == 0 or self.ammo_number <= 0 or self.tooClose == True) and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.gamestate = 0
                elif len(self.aliens) == 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.gamestate += 1
                    Game_b(self.gamestate,self.score_number,self.ammo_number)
                    self.gamestate = 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and self.pause == -1:
                    self.gamestate = 0
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p and self.pause == -1:
                    self.pause *= -1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL and self.ammo_number != 0:
                    self.bullets.append(Bullet(self,self.player2.pos[0]+23,self.player2.pos[1]))
                    channel_game3.play(pygame.mixer.Sound("mygun.wav"))
                    channel_game3.set_volume(0.5)






            #ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            self.shot += self.tps_clock.tick()+0.000000003*(self.gamestate-1) / 1.0
            self.supertime += self.tps_clock.tick() / 1.0

            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            while(self.shot >= 0.001 / self.tps_max and len(self.aliens)!=0 and (self.lives_number != 0 and self.ammo_number > 0) and self.tooClose == False and self.pause == 1):
                self.shot = 0
                channel_game.play(pygame.mixer.Sound("shot.wav"))
                channel_game.set_volume(0.5)
                self.alienbulets.append(AlienBullet(self,self.aliens[los].x,self.aliens[los].y))

            while self.supertime >= 0.001 / self.tps_max:
                self.supertime = -2
                if(len(self.superalien)==0 and self.tooClose == False and self.lives_number !=0 and self.ammo_number > 0 and self.pause == 1):
                    self.superalien.append(SuperAlien(self))
                    channel_game2.play(pygame.mixer.Sound("supersound.wav"))
                    channel_game2.set_volume(0.3)

            #rendering
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        if (self.lives_number != 0 and self.ammo_number > 0 and len(self.aliens) !=0 and self.tooClose == False and self.pause == 1):
            self.edge = False
            self.player.tick()
            self.player2.tick()
            for i in range(0,len(self.aliens)):
                self.aliens[i].move()
                if (self.aliens[i].x >= self.SCREEN_SIZE[0] - 50) or (self.aliens[i].x <= 0):
                    self.edge = True
            if self.edge:
                for i in range(0, len(self.aliens)):
                    if self.aliens[i].x >= self.SCREEN_SIZE[0]-100:
                        self.aliens[i].x -= 10
                    elif self.aliens[i].x < 50:
                        self.aliens[i].x +=10
                    self.aliens[i].shiftDown()
                    if (self.aliens[i].y > 600 ):
                        self.tooClose = True
            for i in range(0,len(self.bullets)):
                self.bullets[i].tick()
            for i in range(0,len(self.alienbulets)):
                self.alienbulets[i].tick()
            for i in range(0,len(self.superalien)):
                self.superalien[i].move()

    def draw(self):
        self.player.draw()
        self.player2.draw()
        self.lives.draw(self.lives_number)
        self.score.draw(self.score_number)
        self.ammo.draw(self.ammo_number)


        for i in range(0,len(self.walls)-1):
            self.walls[i].draw()

        for i in range(0,len(self.bullets)):
            self.bullets[i].draw()
            for j in range(0, len(self.aliens)):
                if(self.bullets[i].hits(self.aliens[j])):
                    self.aliens[j].destroy()
                    self.bullets[i].destroy()
                    self.score_number +=10
                    #self.ammo_number += 1
            for j in range(0, len(self.walls)):
                if (self.bullets[i].hits_wall(self.walls[j])):
                    self.bullets[i].destroy()
                    self.ammo_number -=1
                    if (self.walls[j].state > 0):
                        self.walls[j].state -= 1
                    else:
                        self.walls[j].destroy()
            for j in range(0,len(self.superalien)):
                if(self.bullets[i].hits_super(self.superalien[j])):
                    self.superalien[j].destroy()
                    self.bullets[i].destroy()
                    self.score_number +=100
                    self.ammo_number += 4

            if(self.bullets[i].y <= 0):
                self.bullets[i].destroy()
                self.ammo_number -= 1

        for i in range(0,len(self.aliens)):
            self.aliens[i].draw()

        for i in range(len(self.bullets)-1,-1,-1):
            if(self.bullets[i].toDestroy):
                self.bullets.pop(i)

        for i in range(len(self.aliens)-1,-1,-1):
            if(self.aliens[i].toDestroy):
                self.aliens.pop(i)
                self.rand_opp -= 1

        for i in range(len(self.walls)-1,-1,-1):
            if(self.walls[i].toDestroy):
                self.walls.pop(i)

        for i in range(len(self.alienbulets)-1,-1,-1):
            if(self.alienbulets[i].toDestroy):
                self.alienbulets.pop(i)

        for i in range(len(self.superalien)-1,-1,-1):
            if(self.superalien[i].toDestroy):
                self.superalien.pop(i)

        for i in range(0,len(self.superalien)):
            self.superalien[i].draw()
            if self.superalien[i].x < -65:
                self.superalien[i].destroy()

        for i in range(0,len(self.alienbulets)):
            self.alienbulets[i].draw()
            if(self.alienbulets[i].hits(self.player) or self.alienbulets[i].hits(self.player2) and len(self.aliens) != 0):
                self.alienbulets[i].destroy()
                self.lives_number -= 1
                self.ammo_number -= 4*(self.gamestate)
                self.score_number -= 100
            for j in range(0,len(self.walls)):
                if(self.alienbulets[i].hits_wall(self.walls[j])):
                    self.alienbulets[i].destroy()
                    if(self.walls[j].state>0):
                        self.walls[j].state -=1
                    else:
                        self.walls[j].destroy()

            if (self.alienbulets[i].y >= 720):
                self.alienbulets[i].destroy()

        if self.lives_number == 0 or self.ammo_number <= 0 or self.tooClose:
            self.gameover.draw()
        if len(self.aliens) == 0:
            self.nextlevel.draw()
        if self.pause == -1:
            self.pauseSign.draw()