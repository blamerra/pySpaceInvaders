import pygame
from random import random
from settings import Settings


class Player(pygame.sprite.Sprite):
    SETTINGS = Settings()
    sound = []

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self.SETTINGS.player_image)
        self.rect = self.image.get_rect()
        self.rect.x = (self.SETTINGS.screen_width - (self.rect.width // 2)) // 2
        self.rect.y = (self.SETTINGS.screen_height - 100)

        self.player_speed = self.SETTINGS.player_speed
        self.player_vertical_move = self.SETTINGS.player_vertical_move

    def move_up(self):
        if (self.rect.y > 0) & self.player_vertical_move:
            self.rect.y -= self.player_speed

    def move_down(self):
        if (self.rect.y < self.SETTINGS.screen_height - self.rect.height) & self.player_vertical_move:
            self.rect.y += self.player_speed

    def move_right(self):
        if self.rect.x < self.SETTINGS.screen_width - self.rect.width - self.SETTINGS.player_image_x_margin:
            self.rect.x += self.player_speed

    def move_left(self):
        if self.rect.x >= self.SETTINGS.player_image_x_margin:
            self.rect.x -= self.player_speed

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
