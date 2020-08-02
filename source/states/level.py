#等级关卡阶段

import pygame
from .. import setup
from .. import tools
from .. import constants as C
from ..components import info


class Level:
    def __init__(self):
        self.finished = False
        self.next = None

    def update(self, surface, keys):
        #print("3")
        self.draw(surface)

    def draw(self, surface):
        surface.fill((0, 255, 0))



