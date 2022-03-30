from shutil import move
from termios import CINTR
import pygame

pygame.init()
pygame.display.set_caption("Tank Game")
icon = pygame.image.load("tank.png")
pygame.display.set_icon(icon)



WIDTH, HEIGHT = 800, 600
SPEED = 3
CLOCK = pygame.time.Clock()

wn = pygame.display.set_mode((WIDTH, HEIGHT))

tank_image_U = pygame.image.load('tank_U.png').convert_alpha()
tank_image_R = pygame.image.load('tank_R.png').convert_alpha()
tank_image_D = pygame.image.load('tank_D.png').convert_alpha()
tank_image_L = pygame.image.load('tank_L.png').convert_alpha()

tank_image = tank_image_U
tank = tank_image.get_rect()


bullet_image = pygame.image.load("bullet.png").convert_alpha()
bullet = bullet_image.get_rect()

def place_bullet(x, y):
    wn.blit(bullet, (x, y))
bullet_on_screen = False
bullet_y = 0
bullet_x = 0

def movement(direction):
    global tank_image
    if direction == 'L': # Left
        tank_image = tank_image_L
        if tank.left - SPEED >= 0:
            tank.x -= SPEED
    elif direction == 'R': # Right
        tank_image = tank_image_R
        if tank.right + SPEED <= WIDTH:
            tank.x += SPEED
    elif direction == 'U': # Up
        tank_image = tank_image_U
        if tank.top - SPEED >= 0:
            tank.y -= SPEED
    else: # Down
        tank_image = tank_image_D
        if tank.bottom + SPEED <= HEIGHT:
            tank.y += SPEED

running = True

while running:
    #Red,Green,Blue
    wn.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    #Movement and Rotation
    if keys[pygame.K_a]: # left
        movement('L')
    if keys[pygame.K_d]: # right
        movement('R')
    if keys[pygame.K_w]: # up
        movement('U')
    if keys[pygame.K_s]: # down
        movement('D')
    

    wn.blit(tank_image, tank)
        
    if bullet_on_screen:
        place_bullet(bullet_x, bullet_y)
        bullet_y -= 1
    pygame.display.update()
    CLOCK.tick(90)
