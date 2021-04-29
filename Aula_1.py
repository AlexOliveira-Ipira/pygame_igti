backgoud_imagens_file = 'Imagens/Back.jpeg'
mouse_imagens_file = 'Imagens/Cursor.jpeg'

import pygame
from pygame.locals import *
from sys import exit

#Iniciando o console
pygame.init()

#Definindo o tamanho da tela
screen = pygame.display.set_mode((720,640))

#Definindo um nome para a tela
pygame.display.set_caption('Olá, Mundo Game!')

#definindo a imagem backgroude e convertendo para o mesmo formato do display
backgroung = pygame.image.load(backgoud_imagens_file).convert()

""" Definindo a imagena do cursos, utilizar para testar movimento na tela
    a opção de conver_alpha permite que a imagem seja desenhada """
mouse_cursor = pygame.image.load(mouse_imagens_file).convert_alpha()

#Iniciando o loop

while True:
    for event in pygame.event.get():#for esperando o eento de fechar a tela.
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Coloca o background na tela
    screen.blit(backgroung, (0,0))
    #Obtem as posições do mouse na tela
    x, y = pygame.mouse.get_pos()
    
    #Coloca a imagen no centro do cursor
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    
    #Colocar o cursor com a imagem na tela
    screen.blit(mouse_cursor, (x,y))
    
    #Realiza o update da tela
    pygame.display.update()
    