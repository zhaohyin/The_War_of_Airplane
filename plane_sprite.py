import pygame
import random

# set constant
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT


class Plane_Sprites(pygame.sprite.Sprite):

    # The initialization of Plane_Sprites
    def __init__(self, image_name, speed=1):

        # superclass init function
        super().__init__()

        # Attribute of object
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    # Movement of sprites
    def update(self):
        self.rect.y += self.speed


class Background(Plane_Sprites):

    # simplify the movement of plane
    def __init__(self, isalt = False):
        super().__init__("/Users/Star/Desktop/python/The_War_of_Airplane/images/background.png")
        if isalt == True:
            self.rect.y = -self.rect.height

    def update(self):
        # superclass update function
        super().update()

        # extra action
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Enemy(Plane_Sprites):

    # initialization
    def __init__(self):
        # 1. superclass
        super().__init__("/Users/Star/Desktop/python/The_War_of_Airplane/images/enemy1.png")
        # 2. position
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)
        self.rect.bottom = 0
        # 3. speed
        self.speed = random.randint(2,3)

    def update(self):
        # 1. movement of enemy
        super().update()

        # 2. out of window? -> Y: kill sprite
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    # display information if sprites were killed
    def __del__(self):
        #print("enemy is killed %s " % self.rect)
        pass

class Hero(Plane_Sprites):
    def __init__(self):

        # 1. superclass
        super().__init__("/Users/Star/Desktop/python/The_War_of_Airplane/images/me1.png",0)

        # 2. position
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 100

        # 3. bullet sprites Group
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 3. speed
        self.rect.x += self.speed

        # 4. box of hero
        if self.rect.left <= SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        for i in (range(0,3,1)):
            # 1. create bullet sprite
            bullet = Bullet()

            # 2. position: 3 bullets
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3. add sprite to sprites
            self.bullets.add(bullet)

        pass

class Bullet(Plane_Sprites):

    def __init__(self):

        # set speed && picture
        super().__init__("/Users/Star/Desktop/python/The_War_of_Airplane/images/bullet1.png",-2)

    def update(self):

        super().update()

        # bullet is out of screen
        if self.rect.bottom<0:
            self.kill()

    def __del__(self):
        #print("bullet is destroyed")
        pass

