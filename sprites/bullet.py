import pygame
from settings import Settings


class Bullet(pygame.sprite.Sprite):
    settings = Settings()

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self.settings.bullet_image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -self.rect.height #ocultamos la imagen fuera de la pantalla
        self.speed = self.settings.bullet_speed
        self.status = 0

    def fire(self, x, y):
        if self.status == 0:
            self.rect.x = x
            self.rect.y = y
            self.status = 1

    def update(self):
        if self.rect.y > -self.rect.height and self.status == 1:
            self.rect.y -= self.speed
        else:
            self.status = 0
