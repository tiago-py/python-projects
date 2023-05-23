import pygame
import time
import random
import os 
pygame.font.init()

win = pygame.display.set_mode((750,750))#tamanho e altura da tela
pygame.display.set_caption("Space invaders")

#carregando imagens
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets/red.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets/green.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets/yellow.png"))
#Main
MAIN_SPACE_SHIP = pygame.image.load(os.path.join("assets/player.png"))
RED_LASER = pygame.image.load(os.path.join("assets/pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets/pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets/pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets/pixel_laser_yellow.png"))


background = pygame.transform.scale(pygame.image.load(os.path.join("assets/background-black.png")), (750, 750))

class Ship:
    def __init__(self, x, y, color, health=100):
        pass


def main():
    run = True
    level = 0
    lives = 8
    main_font = pygame.font.Font("font/Pixeled.ttf", 20)
    clock = pygame.time.Clock()
    def redraw_window():
        win.blit(background, (0,0))
        #adicionando o texto na tela
        lives_label = main_font.render(f"Lives: {lives}",1,(255,255,255))
        level_label = main_font.render(f"Level: {level}",1,(255,255,255))
        win.blit(lives_label, (10, 10))
        win.blit(level_label, (750-level_label.get_width()-10, 10))
        pygame.display.update()

    while run:
        clock.tick(60)#fps
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False




main()