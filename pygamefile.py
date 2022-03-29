import pygame, time

# Intialize the pygame
pygame.init()

# Create a window
wn = pygame.display.set_mode((800,600))

# Creating the tank1
tank1 = pygame.image.load('tank1.png')
tank1X = 368
tank1Y = 500
tank1Xchange = 0
tank1Ychange = 0
def place_tank1(x, y):
    wn.blit(tank1, (x, y))

# Create the bullet
bullet = pygame.image.load("bullet.png")

def place_bullet(x, y):
    wn.blit(bullet, (x, y))
#place bullet on screen or not
bullet_on_screen = False
bullet_y = 0
bullet_x = 0

pygame.display.set_caption("Tank Game")# Title
# Image Icon
icon = pygame.image.load("tank.png")
pygame.display.set_icon(icon)

running = True

while running:
    #Red,Green,Blue
    wn.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                tank1Xchange = 0.5
            elif event.key == pygame.K_LEFT:
                tank1Xchange = -0.5
            if event.key == pygame.K_UP:
                tank1Ychange = -0.5
            elif event.key == pygame.K_DOWN:
                tank1Ychange = 0.5
            if event.key == pygame.K_SPACE:
                bullet_on_screen = True
                bullet_x = tank1X + 24
                bullet_y = tank1Y - 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                tank1Xchange = 0
                tank1Ychange = 0
    if not ((tank1X < 0 and tank1Xchange < 0) or (tank1X > 736 and tank1Xchange > 0)):
        tank1X += tank1Xchange
    tank1Y += tank1Ychange
    place_tank1(tank1X, tank1Y)
    if bullet_on_screen:
        place_bullet(bullet_x, bullet_y)
        bullet_y -= 1
    pygame.display.update()
    time.sleep(0.001)
