#主菜单阶段
# 状态机的三个要点：1 此时是什么状态；2 这个状态能干什么 ； 3 这个状态是如何改变的
# 出生，运作，结束

import pygame
from .. import setup
from .. import tools
from .. import constants as C
from ..components import info

class MainMenu:
    def __init__(self):
        self.setup_backgroud()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info("main_menu")
        self.finished = False
        self.next = 'load_screen'

    def setup_backgroud(self):
        self.background = setup.GRAPHICS['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background,(int(self.background_rect.width * C.BG_MULTI),int(self.background_rect.height * C.BG_MULTI)))

        self.viewport = setup.SCREEN.get_rect()
        self.caption = tools.get_images(setup.GRAPHICS['title_screen'],1,60,176,88,(222,54,213),C.BG_MULTI)

    def setup_player(self):
        self.player_image = tools.get_images(setup.GRAPHICS['mario_bros'],178, 32, 12, 16, (0, 0, 0),C.BG_MULTI)

    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        #self.cursor = tools.get_images(setup.GRAPHICS['item_objects'], 25, 160, 8, 8, (0,0,0), C.BG_MULTI)
        self.cursor.image = tools.get_images(setup.GRAPHICS['item_objects'], 24, 160, 8, 8, (0,0,0), C.BG_MULTI)
        rect = self.cursor.image.get_rect()
        rect.x ,rect.y = (220, 360)
        self.cursor.rect = rect
        #状态
        self.cursor.state = "1P"


    def update_cursor(self, keys):
        if keys[pygame.K_UP]:
            self.cursor.state = "1P"
            self.cursor.rect.y = 360
        elif keys[pygame.K_DOWN]:
            self.cursor.state = "2P"
            self.cursor.rect.y = 405
        elif keys[pygame.K_RETURN]:  #main_menu 的状态切换
            if self.cursor.state == "1P":
                self.finished = True
                #print("1P")
            elif self.cursor.state == "2P":
                self.finished = True
                #print("2P")


    def update(self, surface, keys):
        #import random
        #surface.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.update_cursor(keys)
        surface.blit(self.background, self.viewport)
        surface.blit(self.caption, (170,100))
        surface.blit(self.player_image, (110, 490))
        surface.blit(self.cursor.image, self.cursor.rect)

        # self.info.create_label("a")
        # self.info.update()
        self.info.draw(surface)
        #print("main_menu_update")





