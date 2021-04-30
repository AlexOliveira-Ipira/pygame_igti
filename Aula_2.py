import pygame
from pygame.locals import *
from sys import exit

backgroud_imagem_filname = 'Imagens/Imagem1.jpg'

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
backgroud = pygame.image.load(backgroud_imagem_filname).convert()

Fullscreen = False

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if event.type == KEYDOWN:
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((640, 480), 0 , 32)
    screen.blit(backgroud, (0,0))
    pygame.display.update()
    
        
        