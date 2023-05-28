import pygame
from pygame import Rect
import colors
from points import Point
from typing import List
import math

# CONFIG VARS
RADIUS = 50

point_list: List[Point] = [Point(300, 300), Point(100, 300), Point(100, 100), Point(300, 100), Point(300, 300)]

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill(colors.SCREEN)
pygame.display.update()

rect = Rect(290, 290, 20, 20)

pygame.draw.rect(screen, colors.BOT, rect)

# state functions/vars

current_segment = 0

def compute_quadratic_coefficients(m1, b1, p, q):
    a = m1**2+1
    b = m1*b1 - m1*q - p
    c = q**2 - RADIUS**2 + p**2 - 2 * b1 * q + b1**2
    return compute_quadratic_formula(a,b,c)

def compute_quadratic_formula(a, b, c):
    solutions_list = []
    try:
        disc = math.sqrt(b**2 - 4*a*c)
    except:
        raise Exception("too far ig")
    denom = 2*a
    if math.isclose(disc, 0): 
        solutions_list.append(-b/denom)
        return solutions_list
    
    solutions_list.append((-b-disc)/denom)
    solutions_list.append((-b+disc)/denom)

    return solutions_list



def find_next_goal():
    p, q = rect.center
    
    #find current segment information
    m1 = (point_list[current_segment+1].y - point_list[current_segment].y)/(point_list[current_segment+1].x - point_list[current_segment].x)
    b1 = (point_list[current_segment].y) / (point_list[current_segment].x*m1)

    sol_list = compute_quadratic_coefficients(m1, b1, p, q)

    m2 = b2 = None
    if current_segment<len(point_list)-2:
        m2 = (point_list[current_segment+2].y - point_list[current_segment+1].y)/(point_list[current_segment+2].x - point_list[current_segment+1].x)
        b2 = (point_list[current_segment+1].y) / (point_list[current_segment+1].x*m1)
        sol_list_2 = compute_quadratic_coefficients(m2, b2, p, q)
        sol_list = sol_list_2 + sol_list

    
    # loop through each line - check for intersection, check for segment restrictions, 

def getHeading():
    pass


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