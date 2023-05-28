import pygame
from pygame import Rect
import colors
from points import Point
from typing import List

# CONFIG VARS
RADIUS = 50



pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill(colors.SCREEN)
pygame.display.update()

rect = Rect(290, 290, 20, 20)

pygame.draw.rect(screen, colors.BOT, rect)

# state functions

def getHeading():
    rect.


point_list: List[Point] = [Point(300, 300), Point(100, 300), Point(100, 100), Point(300, 100), Point(300, 300)]

for ix,point in enumerate(point_list):
    if ix==len(point_list)-1: continue
    pygame.draw.line(screen, colors.LINE, point, point_list[ix+1])

# pygame.draw.circle(screen, colors.LINE, rect.center, RADIUS, width=0)

running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: running = False

    pygame.display.flip()

pygame.quit()