import pygame

pygame.init()
pygame.display.set_caption("Tank Game")
icon = pygame.image.load("tank.png")
pygame.display.set_icon(icon)



WIDTH, HEIGHT = 800, 600
TANK_SPEED = 3
BULLET_SPEED = 8
CLOCK = pygame.time.Clock()

wn = pygame.display.set_mode((WIDTH, HEIGHT))

tank_image_U = pygame.image.load('tank_U.png').convert_alpha()
tank_image_R = pygame.image.load('tank_R.png').convert_alpha()
tank_image_D = pygame.image.load('tank_D.png').convert_alpha()
tank_image_L = pygame.image.load('tank_L.png').convert_alpha()

tank_image = tank_image_U
tank = tank_image.get_rect()
tank_direction = 'U'


bullet_image_U = pygame.image.load("bullet_U.png").convert_alpha()
bullet_image_R = pygame.image.load("bullet_R.png").convert_alpha()
bullet_image_D = pygame.image.load("bullet_D.png").convert_alpha()
bullet_image_L = pygame.image.load("bullet_L.png").convert_alpha()

bullet_image = bullet_image_U
bullet = bullet_image.get_rect()
bullet_fired = False


def tank_movement():
    global tank_image, bullet_image
    if tank_direction == 'L': # Left
        tank_image = tank_image_L
        if tank.left - TANK_SPEED >= 0:
            tank.x -= TANK_SPEED
    elif tank_direction == 'R': # Right
        tank_image = tank_image_R
        if tank.right + TANK_SPEED <= WIDTH:
            tank.x += TANK_SPEED
    elif tank_direction == 'U': # Up
        tank_image = tank_image_U
        if tank.top - TANK_SPEED >= 0:
            tank.y -= TANK_SPEED
    else: # Down
        tank_image = tank_image_D
        if tank.bottom + TANK_SPEED <= HEIGHT:
            tank.y += TANK_SPEED

def bullet_firing(direction):
    global bullet_fired
    if direction == 'L': # Left
        bullet_image = bullet_image_L
        if bullet.left - BULLET_SPEED >= 0:
            bullet.x -= BULLET_SPEED
        else:
            bullet_fired = False
    elif direction == 'R': # Right
        bullet_image = bullet_image_R
        if bullet.right + BULLET_SPEED <= WIDTH:
            bullet.x += BULLET_SPEED
        else:
            bullet_fired = False
    elif direction == 'U': # Up
        bullet_image = bullet_image_U
        if bullet.top - BULLET_SPEED >= 0:
            bullet.y -= BULLET_SPEED
        else:
            bullet_fired = False
    else: # Down
        bullet_image = bullet_image_D
        if bullet.bottom + BULLET_SPEED <= HEIGHT:
            bullet.y += BULLET_SPEED
        else:
            bullet_fired = False

    wn.blit(bullet_image, bullet)


        

        


running = True

while running:
    #Red,Green,Blue
    wn.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    #tank_movement and Rotation
    if keys[pygame.K_a] or keys[pygame.K_LEFT]: # left
        tank_direction = 'L'
        tank_movement()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # right
        tank_direction = 'R'
        tank_movement()
    if keys[pygame.K_w] or keys[pygame.K_UP]: # up
        tank_direction = 'U'
        tank_movement()
    if keys[pygame.K_s] or keys[pygame.K_DOWN]: # down
        tank_direction = 'D'
        tank_movement()
    if keys[pygame.K_SPACE]: #bullet
        if bullet_fired == False:
            bullet_fired = True
            bullet_direction = tank_direction
            bullet.center = tank.center

    
    wn.blit(tank_image, tank)

    if bullet_fired:
        bullet_firing(bullet_direction)
    
    pygame.display.update()
    CLOCK.tick(90)
