import pygame


class Asset:
    def __init__(self, game, scr):
        self.pygame = game
        self.img = None
        self.x = 0
        self.y = 0
        self.change = 0
        self.screen = scr
        self.speed = 0.5
        self.width = 64
        self.height = 64

    def load_image(self, image_name):
        self.img = pygame.image.load(image_name)

    def render(self):
        screen.blit(playerImg, (self.x, self.y))


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 0.5
PLAYER_SIZE = 64

# Initialize game
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

# Screen
icon = pygame.image.load("media/img/ico.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("media/img/background.png").convert()
screen.blit(background, (0, 0))

# Player
playerImg = pygame.image.load("media/img/spaceship.png")
playerX = SCREEN_WIDTH / 2 - PLAYER_SIZE / 2
playerY = SCREEN_HEIGHT - PLAYER_SIZE - SCREEN_HEIGHT * 0.1
playerChange = 0

# Player Class
player = Asset(pygame, screen)
player.x = SCREEN_WIDTH / 2 - PLAYER_SIZE / 2
player.y = SCREEN_HEIGHT - PLAYER_SIZE - SCREEN_HEIGHT * 0.1
player.load_image("media/img/spaceship.png")


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
    screen.blit(background, (0, 0))
    playerX = player_get_position(playerX, playerChange)
    player(playerX, playerY)
    pygame.display.update()
