import pygame
from pygame.locals import *
from sys import exit

backgroud_imagem_filname = 'Imagens/Imagem1.jpg'

SCREEN_SIZE = (640, 480)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

background = pygame.image.load(backgroud_imagem_filname).convert()

while True:
    
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption('Janel modificada para '+str(event.size))
    
    screen_width, screen_height = SCREEN_SIZE
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background,(x, y))
    
    pygame.display.update()
    
