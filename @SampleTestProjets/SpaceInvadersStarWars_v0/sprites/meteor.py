import pygame
import random

from settings import Settings


class Meteor(pygame.sprite.Sprite):
    SETTINGS = Settings()
    SIZE = [(16, 16), (32, 32), (64, 64), (96, 96)]

    def __init__(self, image):
        super().__init__()
        # self.image = pygame.image.load(self.SETTINGS.meteor_image).convert()
        self.image = image
        self.meteor_size = self.SIZE[random.randrange(0, len(self.SIZE) - 1, 1)]
        self.image = pygame.transform.scale(image, self.meteor_size)
        self.image.set_colorkey(self.SETTINGS.BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = -600

        self.orientation_x = 0
        self.orientation_y = 1

        self.min_speed = 1
        self.max_speed = 3
        self.speed_increment = 1
        self.speed = random.randrange(self.min_speed, self.max_speed, 1)

    def is_inside_screen_limit(self):
        return_value = True
        # Vertical limit
        if (self.rect.x > self.SETTINGS.screen_width + 50) or (self.rect.x < -50):
            return_value = False
        elif (self.rect.y > self.SETTINGS.screen_height + 50) or (self.rect.y < -500):
            return_value = False
        return return_value

    def rotate_horizontal(self):
        self.orientation_x = -1 * random.randrange(-1, 2, 1)
        self.image = pygame.transform.rotate(self.image, 90)

    def rotate_vertical(self):
        self.orientation_y = -1 * random.randrange(-1, 2, 1)
        self.image = pygame.transform.rotate(self.image, 90)

    def increase_speed(self):
        self.min_speed += self.speed_increment
        self.max_speed += self.speed_increment
        self.speed = random.randrange(self.min_speed, self.max_speed, 1)

    def update(self):

        # Change direction lottery
        if random.random() < 0.009:
            self.rotate_horizontal()

        if random.random() < 0.009:
            self.rotate_vertical()

        # Speed lottery
        if random.random() < 0.001:
            self.increase_speed()

        # Movement
        self.rect.x += self.speed * self.orientation_x
        self.rect.y += self.speed * self.orientation_y

        # Si el meteoro llega al final de pantalla se recrea
        if not self.is_inside_screen_limit():
            self.rect.x = random.randrange(50, self.SETTINGS.screen_width - 50, 10)
            self.rect.y = random.randrange(-500, -300, 10)
