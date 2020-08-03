#装载阶段

import pygame
from .. import setup
from .. import tools
from .. import constants as C
from ..components import info

class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = 'level'
        self.timer = 0
        self.info = info.Info('load_screen')

    def update(self, surface, keys):

        self.draw(surface)

        #print("load_screen_update")
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer > 4000:
            self.finished = True
            self.timer = 0

        self.info.draw(surface)

    def draw(self, surface ):
        surface.fill((0, 0, 0))