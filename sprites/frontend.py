import pygame
from settings import Settings


class Frontend(pygame.sprite.Sprite):
    SETTINGS = Settings()

    def __init__(self, screen):
        super().__init__()

        color_black = (0, 0, 0)
        self.rectangle_height = self.SETTINGS.screen_height

        # Create transparent surface
        self.image = pygame.Surface((self.SETTINGS.screen_width, (self.SETTINGS.screen_height * 2))).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        rectangle = pygame.Rect(0, 0, self.SETTINGS.screen_width, self.rectangle_height * 1.4)
        self.rect = pygame.draw.rect(self.image, color_black, rectangle)

        # Animation seed
        self.speed = 4

    def update(self):
        if self.rect.y < self.rectangle_height:
            self.rect.y -= self.speed
