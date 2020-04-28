#Importing and Intizaliving Pygame
import pygame
import random
pygame.init()

#Impoert
attack_animation = [pygame.image.load("Aang 1.png"), pygame.image.load("Aang 2.png"),
                        pygame.image.load("Aang 3.png"), pygame.image.load("Aang 4.png"),
                        pygame.image.load("Aang 5.png"), ]

firesound = pygame.mixer.Sound("Firesound.wav")

watersound = pygame.mixer.Sound("WaterDrop.wav")

airsound = pygame.mixer.Sound("Airsound.wav")


class User_char(pygame.sprite.Sprite):
    '''This is the sprite class that creates the user character, tracks it's position and draws it, it also responsible for cheaking if the user has attacked and chaning the spirte, and cheaking if the sprite has been hit'''
    def __init__(self):
        self.passed = 0
        self.level_row = 5
        self.Generator = 12
        self.Attacking = False
        self.row = 3
        self.image_count = 0
        self.hit = False
        self.attacking = False

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Aang 1.png")

        self.rect = self.image.get_rect()
        self.rect.left = 98
        self.rect.top = 96 * self.row

    def update(self, direction, surface ):

        if direction == 0:
            for pose in range(4):
                self.image = attack_animation[pose]
                surface.blit(self.image, (98, 96*self.row))
            for back_pose in range(-1,-6,-1):
                self.image = attack_animation[back_pose]
                surface.blit(self.image, (98, 96 * self.row))


        if direction == 1 and (self.row + 1) != 5 :
            new_row = 96 * (self.row + 1 )
            self.row = new_row/96
            self.rect.top = new_row

        if direction == -1 and (self.row - 1) != -1:
            new_row = 96 * (self.row - 1 )
            self.row = new_row/96
            self.rect.top = new_row



class Bending_Attack(pygame.sprite.Sprite):
    '''This is a class that randomly sends the generated projectile across the screen by outline it's path'''
    def __init__(self, direction, type, aang_y):
        self.direction = direction
        if type == 1:
            self.type = "Air"
            airsound.set_volume(8)
            airsound.play(0)
        elif type == 2:
            self.type = "Water"
            watersound.set_volume(8)
            watersound.play(0)
        elif type == 3:
            self.type = "Earth"
        elif type == 4:
            self.type = "Fire"
            firesound.set_volume(8)
            firesound.play(0)

        if direction >= 1:
            self.x = 180

        self.y = aang_y * 96

        pygame.sprite.Sprite.__init__(self)

        if self.type == "Air":
            self.image = pygame.image.load("Air.png")


        if self.type == "Water":
            self.image = pygame.image.load("Water.png")

        if self.type == "Earth":
            self.image = pygame.image.load("Earth.png")

        if self.type == "Fire":
            self.image = pygame.image.load("Fire.png")

        self.rect = self.image.get_rect()
        self.rect.left = 100
        self.rect.top =  self.y

    def update(self):
        self.x += self.direction

class Computer_Attack(pygame.sprite.Sprite):
    '''This is a class that randomly sends the generated projectile across the screen by outline it's path'''
    def __init__(self, direction, type, aang_y):
        self.direction = direction
        if type == 1:
            self.type = "Air"
            self.beat = "Fire"
        elif type == 2:
            self.type = "Water"
            self.beat = "Air"
        elif type == 3:
            self.type = "Earth"
            self.beat = "Water"
        elif type == 4:
            self.type = "Fire"
            self.beat = "Earth"

        self.x = 640

        self.y = aang_y * 96

        pygame.sprite.Sprite.__init__(self)

        if self.type == "Air":
            self.image = pygame.image.load("Air.png")

        if self.type == "Water":
            self.image = pygame.image.load("Water.png")

        if self.type == "Earth":
            self.image = pygame.image.load("Earth.png")

        if self.type == "Fire":
            self.image = pygame.image.load("Fire.png")

        self.rect = self.image.get_rect()
        self.rect.left = 100
        self.rect.top =  self.y

    def update(self):
        self.x += self.direction


class Score_counter(pygame.sprite.Sprite):
    '''This is a class that is a label and simply fuctions to see if the projectile and the user attack have collided '''
    def __init__(self,message, x_y_center):
        pygame.sprite.Sprite.__init__(self)
        self.counter = 0
        self.__font = pygame.font.SysFont('Calibri', 20)
        self.__message = str(message)
        self.__text = str(message) + str(self.counter)
        self.__center = x_y_center
        self.image = self.__font.render(self.__text, 3, (0,0,0))


    def update(self):
        self.__text =  str(self.__message) + str(self.counter)
        self.image = self.__font.render(self.__text, 3, (0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.__center

