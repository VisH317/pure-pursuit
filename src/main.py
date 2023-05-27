import pygame
from pygame import Rect
import colors
from points import Point
from typing import List

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill(colors.SCREEN)
pygame.display.update()

rect = Rect(275, 275, 50, 50)

pygame.draw.rect(screen, colors.BOT, rect)

point_list: List[Point] = []

running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: running = False

    pygame.display.flip()

pygame.quit()