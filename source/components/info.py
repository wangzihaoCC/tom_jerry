# Label
import pygame
from .. import constants as C
from . import coin

pygame.font.init()

class Info:
    def __init__(self, state):
        self.state = state
        self.create_state_labels()
        self.create_info_labels()
        self.flash_coin = coin.FlashingCoin()


    def create_state_labels(self):
        self.state_labels = []
        if self.state == 'main_menu':
            self.state_labels.append(((self.create_label('1 PLAYER GAME')),(272, 360)))
            self.state_labels.append(((self.create_label('2 PLAYER GAME')), (272, 405)))
            self.state_labels.append(((self.create_label('TOP - ')), (290, 465)))
            self.state_labels.append(((self.create_label('0000000')), (400, 465)))



    def create_info_labels(self):
        self.info_labels = []
        #if self.state == 'main_menu':
        self.info_labels.append((self.create_label('MARIO'),(75,30)))
        self.info_labels.append((self.create_label('WORLD'), (450, 30)))
        self.info_labels.append((self.create_label('TIME'), (625, 30)))
        self.info_labels.append((self.create_label('000000'), (75, 55)))
        self.info_labels.append((self.create_label('x00'), (300, 55)))
        self.info_labels.append((self.create_label('1 - 1'), (480, 55)))

    def create_label(self, label, size=40, width_scale=1.25, height_scale=1):
        font=pygame.font.SysFont(C.fontName, size)
        # try:
        #     font = pygame.font.Font('Fixedsys500c.ttf',size)
        # except OSError:
        #     print("Error: 没有找到文件或读取文件失败")
        #     font = pygame.font.Font('hsfont.ttc', size)

        label_image = font.render(label, 1, (255,255,255))
        rect = label_image.get_rect()
        label_image = pygame.transform.scale(label_image,(int(rect.width * width_scale),int(rect.height * height_scale)))
        return label_image



    def update(self):   #更新分数等
        self.flash_coin.update()

    def draw(self, surface):
        for i in self.state_labels:
            surface.blit(i[0],i[1])
        for i in self.info_labels:
            surface.blit(i[0], i[1])
        surface.blit(self.flash_coin.image, self.flash_coin.rect)
        #surface.blit(self.create_label("Hello world2",size=60),(100,400))