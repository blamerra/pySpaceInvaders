import pygame
from settings import Settings


class Bullet(pygame.sprite.Sprite):
    SETTINGS = Settings()
    STATUS_READY = 0
    STATUS_FIRED = 1
    AMMO_LASER = 0
    AMMO_TORPEDO = 1

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self.SETTINGS.bullet_image).convert_alpha()
        self.sound = pygame.mixer.Sound(self.SETTINGS.bullet_sound)
        self.sound.set_volume(self.SETTINGS.bullet_sound_volume)
        self.sound_channel = pygame.mixer.find_channel()

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -self.rect.height  # ocultamos la imagen fuera de la pantalla
        self.speed = self.SETTINGS.bullet_speed
        self.status = 0

    def fire(self, x, y):
        if self.status == self.STATUS_READY:
            self.sound.stop()
            self.sound_channel.stop()
            self.sound_channel.play(self.sound)

            self.rect.x = x
            self.rect.y = y

            self.status = self.STATUS_FIRED
        else:
            pass
    def set_ready_status(self):
        self.status = self.STATUS_READY
        self.rect.y = -self.rect.height
        self.speed = self.SETTINGS.bullet_speed

    def move(self):
        self.speed += self.speed * self.SETTINGS.bullet_speed_increase
        self.rect.y -= self.speed

    def update(self):
        if self.rect.y > (-self.rect.height) and self.status == self.STATUS_FIRED:
            self.move()
        else:
            self.set_ready_status()
