# assets and original game
# https://github.com/attreyabhatt/Space-Invaders-Pygame

# Tutorial Mundo Python
# https://www.youtube.com/watch?v=MY9Jbri3wnE
# https://github.com/mundo-python/pygame-Scripts/blob/master/17_game_over.py

import pygame


# Sprites test
class Rectangle(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.Surface((200, 200))
        self.image.fill((0, 0, 0))
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        # Actualiza esto cada vuelta de bucle.
        self.rect.y += 10
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT * 0.1)

    def right(self):
        if self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += PLAYER_SPEED

    def left(self):
        if self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.left()
        elif keys[pygame.K_RIGHT]:
            self.right()


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
PLAYER_SPEED = 10
PLAYER_SIZE = 64
PLAYER_IMAGE = "media/img/spaceship.png"
FPS = 60


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

# Music
pygame.mixer.music.load("media/sound/background.wav")
pygame.mixer.music.play(-1)

# FPS control
clock = pygame.time.Clock()


def update_fps():
    font = pygame.font.SysFont("Arial", 18)
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, True, pygame.Color("coral"))
    return fps_text


# Player
playerImg = pygame.image.load("media/img/spaceship.png")
playerX = SCREEN_WIDTH / 2 - PLAYER_SIZE / 2
playerY = SCREEN_HEIGHT - PLAYER_SIZE - SCREEN_HEIGHT * 0.1
playerChange = 0

# Sprites creation
player = Player()
# rectangle = Rectangle()
sprites = pygame.sprite.Group()
sprites.add(player)
'''
player = Asset(pygame, screen)
player.x = SCREEN_WIDTH / 2 - PLAYER_SIZE / 2
player.y = SCREEN_HEIGHT - PLAYER_SIZE - SCREEN_HEIGHT * 0.1
player.load_image("media/img/spaceship.png")
'''


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
        '''

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerChange = -PLAYER_SPEED
            player.left()
            #player.rect.x += -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            playerChange = PLAYER_SPEED
            player.right()
            #player.rect.x += PLAYER_SPEED
        else:
            playerChange = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChange = -PLAYER_SPEED
            if event.key == pygame.K_RIGHT:
                playerChange = PLAYER_SPEED
        '''
    # Render Screen
    screen.blit(background, (0, 0))
    # FPS
    clock.tick(FPS)
    screen.blit(update_fps(), (10, 0))
    playerX = player_get_position(playerX, playerChange)
    player(playerX, playerY)
    sprites.update()
    sprites.draw(screen)
    pygame.display.update()
