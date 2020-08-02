#图片加载方法；扣图方法；

import pygame
import os

class Game:
    def __init__(self, state_dict, start_state):
        self.screen = pygame.display.get_surface()   # 获取对当前设置的显示surface的引用
        self.clock = pygame.time.Clock()  #计时和帧数
        self.keys = pygame.key.get_pressed()
        self.state_dict = state_dict
        self.state = self.state_dict[start_state]  # 这里返回的是一个object，例如这里，state 是 main_menu.MainMenu()
        print(self.state)

    def update(self):
        if self.state.finished:
            #print("finish")
            next_state = self.state.next
            #print(next_state)
            self.state.finished = False
            self.state = self.state_dict[next_state]
            #print(self.state)

        self.state.update(self.screen,self.keys)



    def run(self, state):   #0802
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()


            self.update(self.screen, self.keys)  #0802

            pygame.display.update()
            self.clock.tick(24)

    #加载图片
def load_graphics(path,accept=('.jpg','.png','.gif','.bmp')):   # （路径，允许后缀）
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics

def get_images(sheet,x,y,width,heigh,colorKey,scale):  #从已经加载的图片里，获得图片中的某部分图片
    image = pygame.Surface((width,heigh))    #surface 可以理解为图层
    image.blit(sheet,(0,0), (x,y,width,heigh))
    image.set_colorkey(colorKey)
    image = pygame.transform.scale(image,(int(width*scale),int(heigh*scale)))
    return image
