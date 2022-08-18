import pygame
import random

from settings import Settings


class Meteor(pygame.sprite.Sprite):
    SETTINGS = Settings()

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self.SETTINGS.meteor_image).convert()
        self.image.set_colorkey(self.SETTINGS.BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = -600

        self.orientation_x = 0
        self.orientation_y = 1

        self.min_speed = 1
        self.max_speed = 3
        self.speed_increment = 1
        self.speed = random.randrange(self.min_speed, self.max_speed, 1)

    def update(self):

        # Rotate lottery
        if random.random() < 0.001:
            self.image = pygame.transform.rotate(self.image, 90)

        # Change direction lottery
        if random.random() < 0.009:
            self.orientation_x = -1 * random.randrange(-1, 2, 1)
            self.image = pygame.transform.rotate(self.image, 90)

        if random.random() < 0.009:
            self.orientation_y = -1 * random.randrange(-1, 2, 1)
            self.image = pygame.transform.rotate(self.image, 90)

        # Speed lottery
        if random.random() < 0.001:
            self.min_speed += self.speed_increment
            self.max_speed += self.speed_increment
            self.speed = random.randrange(self.min_speed, self.max_speed, 1)

        # Movement
        self.rect.x += self.speed * self.orientation_x
        self.rect.y += self.speed * self.orientation_y

        # Si el meteoro llega al final de pantalla se recrea

        if (self.rect.y > self.SETTINGS.screen_height + 50) or (self.rect.y < -500) or (self.rect.x > self.SETTINGS.screen_width + 50) or (self.rect.x < -50):
            self.rect.x = random.randrange(50, self.SETTINGS.screen_width-50, 10)
            self.rect.y = random.randrange(-500, -100, 10)



