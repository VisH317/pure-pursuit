import pygame
from pygame import Rect
import colors
from points import Point
from typing import List
import math

# CONFIG VARS
RADIUS = 50

point_list: List[Point] = [Point(300, 300), Point(275, 300), Point(275, 100), Point(300, 100), Point(400, 300)]

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill(colors.SCREEN)
pygame.display.update()

rect = Rect(290, 290, 20, 20)

pygame.draw.rect(screen, colors.BOT, rect)

# state functions/vars

current_segment = 0
angle = 0
current_point = Point(300, 300)

def compute_quadratic_coefficients(m1, b1, p, q, idx):
    a = m1**2+1
    b = m1*b1 - m1*q - p
    c = q**2 - RADIUS**2 + p**2 - 2 * b1 * q + b1**2
    return compute_quadratic_formula(a,b,c, m1, b1, idx)

def compute_coefficients(x1, y1, x2, y2, p, q):
    dx = x2-x1
    dy = y2-y1
    dr = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
    D = (x1-p)*(y2-q) - (x2-p)*(y1-q)

    try:
        print(RADIUS**2 * dr**2 - D**2)
        disc = math.sqrt(RADIUS**2 * dr**2 - D**2)
    except:
        return []


    # solving for x coordinate

    b = dx * disc * (-1 if dy<0 else 1)
    ans_x_1 = ((D*dy)+b)/(dr**2)
    ans_x_2 = ((D*dy)-b)/(dr**2)
    print("stuff: ", dr, ", ", D, ", ", ans_x_1,", ", disc, ", ", b, ", ", dx)

    # solving for y coordinate
    b = abs(dy) * disc
    ans_y_1 = (-D*dx+b)/(dr**2)
    ans_y_2 = (-D*dx-b)/(dr**2)

    if disc==0:
        return [Point(ans_x_1+p, ans_y_1+q)]
    
    return [Point(ans_x_1+p, ans_y_1+q), Point(ans_x_2+p, ans_y_2+q)]


def compute_quadratic_formula(a, b, c, m, b1, idx):
    solutions_list = []
    try:
        disc = math.sqrt(b**2 - 4*a*c)
    except:
        raise Exception("too far ig")
    denom = 2*a
    if math.isclose(disc, 0): 
        x = -b/denom
        y = m*x + b1
        if point_list[idx].x>x or point_list[idx+1].x<x or point_list[idx].y>y or point_list[idx+1].y<y:
            solutions_list.append(Point(x,y))
        return solutions_list
    
    x = (-b-disc)/denom
    y = m*x+b1
    if point_list[idx].x>x or point_list[idx+1].x<x or point_list[idx].y>y or point_list[idx+1].y<y:
        solutions_list.append(Point(x,y))
    x = (-b+disc)/denom
    y = m*x+b1
    if point_list[idx].x>x or point_list[idx+1].x<x or point_list[idx].y>y or point_list[idx+1].y<y:
        solutions_list.append(Point(x,y))

    return solutions_list

def is_closer(target: Point, first: Point, second: Point):
    print("first: ", first, ", second: ", second, ", target: ", target)
    dist1 = math.sqrt((target.x-first.x)**2+(target.y-first.y)**2)
    dist2 = math.sqrt((target.x-second.x)**2+(target.y-second.y)**2)

    return dist1<dist2


def choose_goal_point(sol_list, sol_list_2, idx):
    if len(sol_list_2)==1:
        return sol_list_2[0], True
    elif len(sol_list_2)==2:
        return sol_list_2[0] if is_closer(point_list[idx+2], sol_list_2[0], sol_list_2[1]) else sol_list_2[1], True
    elif len(sol_list)==1:
        return sol_list[0], False
    elif len(sol_list)==2:
        return sol_list[0] if is_closer(point_list[idx+1], sol_list[0], sol_list[1]) else sol_list[1], False



def find_next_goal():
    global current_segment
    p, q = rect.center
    
    #find current segment information
    m1 = (point_list[current_segment+1].y - point_list[current_segment].y)/(point_list[current_segment+1].x - point_list[current_segment].x)
    b1 = (point_list[current_segment].y) - (point_list[current_segment].x*m1)

    # sol_list = compute_coefficients(m1, b1, p, q, current_segment)
    sol_list = compute_coefficients(point_list[current_segment].x, point_list[current_segment].y, point_list[current_segment+1].x, point_list[current_segment+1].y, p, q)

    m2 = b2 = None
    if current_segment<len(point_list)-2:
        # m2 = (point_list[current_segment+2].y - point_list[current_segment+1].y)/(point_list[current_segment+2].x - point_list[current_segment+1].x)
        # b2 = (point_list[current_segment+1].y) / (point_list[current_segment+1].x*m1)
        # sol_list_2 = compute_quadratic_coefficients(m2, b2, p, q, current_segment+1)
        sol_list_2 = compute_coefficients(point_list[current_segment+1].x, point_list[current_segment+1].y, point_list[current_segment+2].x, point_list[current_segment+2].y, p, q)

    print(sol_list)

    goal_point, next = choose_goal_point(sol_list, sol_list_2, current_segment)
    if next: current_segment+=1
    return goal_point

# setup bang bang movement

def move_to_point():
    pass

def getHeading(start: Point, loc: Point):
    y = loc.y - start.y
    x = loc.x - start.x
    return math.atan2(y, x) * 180 / math.pi


for ix,point in enumerate(point_list):
    if ix==len(point_list)-1: continue
    pygame.draw.line(screen, colors.LINE, point, point_list[ix+1])

# pygame.draw.circle(screen, colors.LINE, rect.center, RADIUS, width=0)

first_point = find_next_goal()
print(first_point)
pygame.draw.circle(screen, colors.PATH, Point(300, 300), 50, width=2)
pygame.draw.line(screen, colors.PATH, Point(300, 300), first_point)

running = True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: running = False

    pygame.display.flip()

pygame.quit()