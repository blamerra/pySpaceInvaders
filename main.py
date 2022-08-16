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
        self.rect.topleft = [0, -SCREEN_HEIGHT]
        self.scroll = BACKGROUND_SCROLL
        self.speed = BACKGROUND_SPEED

    def update(self):
        #keys = pygame.key.get_pressed()
        #if keys[SHORTCUT_BACKGROUND_SCROLL_STOP]:
        #    self.scroll = not self.scroll

        if self.scroll:
            if self.rect.y < 0:
                self.rect.y += BACKGROUND_SPEED
            else:
                self.rect.y = -SCREEN_HEIGHT

    def pause(self):
        self.scroll = not self.scroll
class Fps(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH - 10, 10)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)
        self.fps = None
        self.fps_text = None

    def update(self):
        self.image.fill(pygame.Color("black"))

        self.clock.tick(GAME_FPS)
        self.fps = str(int(self.clock.get_fps()))
        self.fps_text = self.font.render(self.fps, True, pygame.Color("coral"))
        self.image.blit(self.fps_text, [0, 0])


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_ICON = "media/img/ico.png"
SCREEN_TITLE = "Space Invaders"

BACKGROUND_IMAGE = "media/img/background_800x1200.png"
BACKGROUND_MUSIC = "media/sound/background.wav"
BACKGROUND_SCROLL = True
BACKGROUND_SPEED = 1
SHORTCUT_BACKGROUND_SCROLL_STOP = pygame.K_b

PLAYER_SPEED = 10
PLAYER_SIZE = 64
PLAYER_VERTICAL_MOVE = True
PLAYER_IMAGE = "media/img/spaceship.png"

GAME_FPS = 60

SHORTCUT_PAUSE = pygame.K_PAUSE

# Initialize game
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

# Screen
icon = pygame.image.load(SCREEN_ICON)
pygame.display.set_icon(icon)
pygame.display.set_caption(SCREEN_TITLE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Music
# TODO descomentar musica
# pygame.mixer.music.load(SCREEN_BACKGROUND_MUSIC)
# pygame.mixer.music.play(-1)


# Sprites creation
player = Player()
background = Background()
fps = Fps()
sprites = pygame.sprite.Group()
sprites.add(background, player, fps)

# Game loop
running = 1
pause = 0
while running:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.KEYDOWN:
            if event.key == SHORTCUT_PAUSE:
                pause = not pause
            if event.key == SHORTCUT_BACKGROUND_SCROLL_STOP:
                background.pause()

    # Render Screen
    if not pause:
        sprites.update()
        sprites.draw(screen)
        pygame.display.update()

pygame.quit()
