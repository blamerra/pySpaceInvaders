import pygame
from settings import Settings
from background import Background
from player import Player
from fps import Fps

# Constants
settings = Settings()

# Initialize game
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])

# Screen
icon = pygame.image.load(settings.screen_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption(settings.screen_title)
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

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
            if event.key == settings.shortcut_pause:
                pause = not pause
            if event.key == settings.shortcut_background_scroll_pause:
                background.pause()

    # Render Screen
    if not pause:
        sprites.update()
        sprites.draw(screen)
        pygame.display.update()

pygame.quit()
