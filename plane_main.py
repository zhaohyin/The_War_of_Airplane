'''
飞机大战游戏的主类，主要任务：
1）封装主游戏类
2）创建游戏对象
3）启动游戏
'''

import random
import pygame
import plane_sprite

pygame.init()

# set constant
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneGame(object):
    # Game of The War of plane

    def __init__(self):

        print("The Initialization of the game")

        # create game window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # create clock
        self.clock = pygame.time.Clock()

        # create sprites group
        self.__create_sprites()

        # create event: enemy appears every 1000ms
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

        # create event: hero fire every 500ms
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites(self):

        # create background sprite 1 & background sprite 2
        bg1 = plane_sprite.Background()
        bg2 = plane_sprite.Background(True)

        self.bg_group = pygame.sprite.Group(bg1, bg2)

        # create enemy sprites
        self.enemy_group = pygame.sprite.Group()

        # create hero sprites
        self.hero = plane_sprite.Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("Game Start")

        while True:
            # 1. set update rate
            self.clock.tick(FRAME_PER_SEC)
            # 2. monitor
            self.__event_handler()
            # 3. collision detection
            self.__collision_dectection()
            # 4. update/draw sprites group
            self.__update_sprites()
            # 5. update display
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # exit
            if event.type == pygame.QUIT:
                self.__game_over()

            # enemy
            if event.type == CREATE_ENEMY_EVENT:
                enemy = plane_sprite.Enemy()

                self.enemy_group.add(enemy)
                #print("enemy begin to appear")

            # hero
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0

            # hero fire
            if event.type == HERO_FIRE_EVENT:
                self.hero.fire()

    def __collision_dectection(self):

        # bullet -> enemy
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)

        # hero -> enemy
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)

        # sprite_list is empty or not?
        if len(enemies) > 0:

            # hero died
            self.hero.kill()

            # game over
            self.__game_over()
        pass

    # update screen
    def __update_sprites(self):

        # update background sprites
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        # update enemy sprites
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # update hero sprites
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # update bullets
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    def __game_over(self):
        print("Game Over")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # create object of game
    game = PlaneGame()

    # start Game
    game.start_game()
