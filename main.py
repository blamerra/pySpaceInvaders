import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 0.5
PLAYER_SIZE = 64

# Initialize game
pygame.init()
icon = pygame.image.load("media/img/ico.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Player
playerImg = pygame.image.load("media/img/spaceship.png")
playerX = SCREEN_WIDTH / 2 - PLAYER_SIZE / 2
playerY = SCREEN_HEIGHT - PLAYER_SIZE - SCREEN_HEIGHT * 0.1
playerChange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def player_get_position(x, change):
    position = min(max(0, x + change), SCREEN_WIDTH)
    return position


# Game loop
running = 1
while running:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

        # TODO Controlar evento key up si se pulsa la otra direccion muy rapido
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerChange = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                playerChange = PLAYER_SPEED

    # Render Screen
    screen.fill((255, 255, 255))
    playerX = player_get_position(playerX, playerChange)
    player(playerX, playerY)
    pygame.display.update()
