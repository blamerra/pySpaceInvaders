import pygame
from settings import Settings


class Bullet(pygame.sprite.Sprite):
    settings = Settings()

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self.settings.bullet_image)
        self.rect = self.image.get_rect()
        self.rect.x = (self.settings.screen_width - (self.rect.width // 2)) // 2
        self.rect.y = (self.settings.screen_height - 100)
        self.speed = self.settings.bullet_speed

    def update(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.rect.y = (self.settings.screen_height - 100)