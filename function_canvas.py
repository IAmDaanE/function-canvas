import pygame
import math

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 650

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Canvas")
clock = pygame.time.Clock()

x = - WINDOW_WIDTH / 2

lines_color = (255,255,255)
graph_color = (255, 0, 0)
background_color = (0,0,0)

x_jump = 0.3

running = True

screen.fill(background_color)
pygame.draw.rect(screen, lines_color, (0,WINDOW_HEIGHT / 2, WINDOW_WIDTH + 1, 1))
pygame.draw.rect(screen, lines_color, (WINDOW_WIDTH / 2, 0, 1, WINDOW_HEIGHT + 1))

def sqrt_graph():
    global x,y,x_jump
    x_jump = 0.1
    if x < 0:
        y = -math.sqrt(-x) * 10
    else: 
        y = math.sqrt(x) * 10

def oscillator():
    global x,y,x_jump
    x_jump = 0.01
    modified_x = x / 45
    y = modified_x * math.sin(modified_x**2) * 5

def chaos():
    global x,y,x_jump
    if x < -25 or x > 25:
        x_jump = 0.1
    else:
        x_jump = 0.001
    modified_x = x / 50
    y = math.sin(1/modified_x)
    y *= 318
    y += 7

def parabola():
    global y, x_jump
    x_jump = 0.1
    modified_x = x / 18
    y = modified_x ** 2 - 100

def heartbeat():
    global y,x_jump
    x_jump = 0.08
    modified_x = x / 20
    y = 5 * math.cos(modified_x) + - math.cos(5 * modified_x)
    y *= 50

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if x == 0:
        x += x_jump

    if x <= WINDOW_WIDTH / 2:
        sqrt_graph()
        x += x_jump
        pygame.draw.rect(screen, graph_color, (WINDOW_WIDTH / 2 + x, WINDOW_HEIGHT / 2 - y, 2, 2))
        pygame.display.update()


