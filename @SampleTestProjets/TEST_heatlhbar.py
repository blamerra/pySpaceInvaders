import pygame
import math
import random
from pygame.locals import *
import colorsys

# setup

background_colour = (255, 255, 255)
(width, height) = (800, 400)

screen = pygame.display.set_mode((width, height))  # ,pygame.FULLSCREEN)
screen.fill(background_colour)
pygame.display.set_caption('Nice colours')

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pos = pygame.mouse.get_pos()

    bar_length = min(abs(pos[0] - 100), width - 200)
    bar_percentage = bar_length / (width - 200)
    h, s, v = 0.33 * bar_percentage, 1, 1
    r, g, b = colorsys.hsv_to_rgb(h, s, v)

    screen.fill(background_colour)

    colour = [int(255 * r), int(255 * g), int(255 * b)]
    pygame.draw.line(screen, colour, [100, height / 2], [100 + bar_length, height / 2], 100)

    pygame.display.flip()

pygame.quit()