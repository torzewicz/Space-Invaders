import pygame
import sys
from game import Game
from game_b import Game_b

class Starting(object):

    def __init__(self):
        self.tps_max = 300.0
        pygame.init()
        self.SCREEN_SIZE = (1280, 720)  # grafiki dopasowane do tego
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)


        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.gamestate = 0
        self.mode = 1

        background = pygame.image.load("tlo2.jpg")
        pygame.mixer.music.load("houston.wav")

        pygame.mixer.music.play(1)

        pygame.mixer.music.set_volume(0.5)
        self.text = open('score','r+').read()


        while (self.gamestate == 0):
            if (pygame.mixer.music.get_busy() == False):
                pygame.mixer.music.load("jaglak.mp3")
                pygame.mixer.music.play(-1)
            for event in pygame.event.get():
                if self.mode == 1 and event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.mode = 2
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.mode ==1:
                    Game(1,0,0)
                    self.text = open('score', 'r+').read()
                elif self.mode == 3 and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and self.mode == 3:
                    self.mode = 2
                elif event.type == pygame.QUIT:
                    sys.exit()
                elif self.mode == 2 and event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.mode = 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.mode == 2:
                    Game_b(1,0,5)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and self.mode == 2:
                    self.mode = 3

            self.tps_delta += self.tps_clock.tick() / 1000.0

            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            self.screen.fill((0, 0, 0))
            self.screen.blit(background, (0, 0))
            self.draw()
            pygame.display.flip()

        self.text.close()
    def tick(self):
        pass

    def draw(self):
        myfont = pygame.font.SysFont("monospace", 50)
        myfont2 = pygame.font.SysFont("monospace",40)
        start = pygame.image.load("start.png")
        button = pygame.image.load("ship.png")
        player = pygame.image.load("player.png")
        player2 = pygame.image.load("player2.png")
        smutny = pygame.image.load("smutny.jpg")
        label = myfont.render("ONE PLAYER", 1, (255, 255, 255))
        label2 = myfont.render("TWO PLAYERS",1,(255,255,255))
        label3 = myfont.render("QUIT",1,(255,255,255))
        label4 = myfont2.render("BEST SCORE:",1,(255,255,255))
        best = myfont2.render(str(int(self.text)),1,(255,255,255))
        self.screen.blit(label, (self.SCREEN_SIZE[0]/2-300,self.SCREEN_SIZE[1]/2))
        self.screen.blit(label2, (self.SCREEN_SIZE[0] / 2 - 300, self.SCREEN_SIZE[1] / 2 + 70))
        self.screen.blit(label3, (self.SCREEN_SIZE[0] / 2 - 300, self.SCREEN_SIZE[1] / 2 +140))
        self.screen.blit(start,(self.SCREEN_SIZE[0]/2-650,self.SCREEN_SIZE[1]/2-500))
        self.screen.blit(label4,(0,0))
        self.screen.blit(best,(270,0))

        if self.mode == 1:
            self.screen.blit(button, (self.SCREEN_SIZE[0] / 2 - 400, self.SCREEN_SIZE[1] / 2))
            self.screen.blit(player, (self.SCREEN_SIZE[0] / 2 + 100, self.SCREEN_SIZE[1] / 2 + 12))
        elif self.mode == 2:
            self.screen.blit(button, (self.SCREEN_SIZE[0] / 2 - 400, self.SCREEN_SIZE[1] / 2 + 70))
            self.screen.blit(player, (self.SCREEN_SIZE[0] / 2 + 100, self.SCREEN_SIZE[1] / 2 + 82))
            self.screen.blit(player2, (self.SCREEN_SIZE[0] / 2 + 180, self.SCREEN_SIZE[1] / 2 + 82))
        elif self.mode == 3:
            self.screen.blit(button, (self.SCREEN_SIZE[0] / 2 - 400, self.SCREEN_SIZE[1] / 2 + 140))
            self.screen.blit(smutny, (self.SCREEN_SIZE[0] / 2 + 100, self.SCREEN_SIZE[1] / 2 + 140))