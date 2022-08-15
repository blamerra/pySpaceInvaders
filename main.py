# assets and original game
# https://github.com/attreyabhatt/Space-Invaders-Pygame

# Tutorial Mundo Python
# https://www.youtube.com/watch?v=MY9Jbri3wnE
# https://github.com/mundo-python/pygame-Scripts/blob/master/17_game_over.py

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT * 0.1)

    def move_up(self):
        if (self.rect.y > 0) & PLAYER_VERTICAL_MOVE:
            self.rect.y -= PLAYER_SPEED

    def move_down(self):
        if (self.rect.y < SCREEN_HEIGHT - self.rect.height) & PLAYER_VERTICAL_MOVE:
            self.rect.y += PLAYER_SPEED

    def move_right(self):
        if self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += PLAYER_SPEED

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BACKGROUND_IMAGE).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]

    def update(self):
        if BACKGROUND_MOVE:
            self.rect.y += 1



# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_ICON = "media/img/ico.png"
SCREEN_TITLE = "Space Invaders"

BACKGROUND_IMAGE = "media/img/background.png"
BACKGROUND_MUSIC = "media/sound/background.wav"
BACKGROUND_MOVE = False

PLAYER_SPEED = 10
PLAYER_SIZE = 64
PLAYER_VERTICAL_MOVE = False
PLAYER_IMAGE = "media/img/spaceship.png"

GAME_FPS = 60

# Initialize game
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

# Screen
icon = pygame.image.load(SCREEN_ICON)
pygame.display.set_icon(icon)
pygame.display.set_caption(SCREEN_TITLE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# TODO crear un sprite para el background y moverlo
# background = pygame.image.load(BACKGROUND_IMAGE).convert()
# screen.blit(background, (0, 0))

# Music
# TODO descomentar musica
# pygame.mixer.music.load(SCREEN_BACKGROUND_MUSIC)
# pygame.mixer.music.play(-1)

# FPS control
game_clock = pygame.time.Clock()


def update_fps():
    font = pygame.font.SysFont("Arial", 18)
    fps = str(int(game_clock.get_fps()))
    fps_text = font.render(fps, True, pygame.Color("coral"))
    return fps_text


# Sprites creation
player = Player()
background = Background()
sprites = pygame.sprite.Group()
sprites.add(background, player)

# Game loop
running = 1
while running:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

    # Render Screen
    #screen.blit(background, (0, 0))
    # FPS
    game_clock.tick(GAME_FPS)
    screen.blit(update_fps(), (10, 0))

    sprites.update()
    sprites.draw(screen)
    pygame.display.update()
    # TODO mirar para que sirve .flip()
    pygame.display.flip()

pygame.quit()
