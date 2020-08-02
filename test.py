import pygame
from pygame.locals import *


pygame.init()

w,h = 500,500
pygame.display.set_mode((w,h),0,32)
screen = pygame.display.get_surface()

bgpc = pygame.image.load("./resources/graphics/bg01.bmp")
bgpc = pygame.transform.scale(bgpc,(w,h))

mario_image = pygame.image.load("./resources/graphics/alien.bmp")

mario = pygame.sprite.Sprite()
mario.image = mario_image
mario.rect = mario.image.get_rect()
mario.rect.x,mario.rect.y = w/2,h/2

player_group = pygame.sprite.Group()
player_group.add(mario)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # pygame.display.quit()
            # quit()
            exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                mario.rect.y += 10

    screen.blit(bgpc,(0,0))
    player_group.draw(screen)
    pygame.display.update()