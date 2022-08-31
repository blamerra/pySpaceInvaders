import pygame
from settings import Settings
from classes.ammo import Ammo


class Bullet(pygame.sprite.Sprite):
    SETTINGS = Settings()
    STATUS_READY = 0
    STATUS_FIRED = 1
    AMMO_LASER = 0
    AMMO_TORPEDO = 1

    def __init__(self):
        super().__init__()
        self.sound = None
        self.speed = None
        self.speed_increase = None
        self.status = self.STATUS_READY

        self.ammo_list = []
        self.ammo_list.append(
                Ammo('laser', self.SETTINGS.ammo_laser_image, self.SETTINGS.ammo_laser_sound, 0.5, 15, 0)
            )
        self.ammo_list.append(
                Ammo('torpedo', self.SETTINGS.ammo_torpedo_image, self.SETTINGS.ammo_torpedo_sound, 1, 1, 0.03)
            )

        self.ammo_active = self.AMMO_LASER
        self.sound_channel = pygame.mixer.find_channel()
        self._update_ammo(self.ammo_active)
        self.rect.x = 0
        self.rect.y = -self.rect.height  # ocultamos la imagen fuera de la pantalla




        '''
        self.image = pygame.image.load(self.SETTINGS.bullet_image).convert_alpha()
        self.sound = pygame.mixer.Sound(self.SETTINGS.bullet_sound)
        self.sound.set_volume(self.SETTINGS.bullet_sound_volume)
        self.sound_channel = pygame.mixer.find_channel()

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -self.rect.height  # ocultamos la imagen fuera de la pantalla
        self.speed = self.SETTINGS.bullet_speed
        self.status = self.STATUS_READY

        self.speed_increase = 0
        '''

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

    def _update_ammo(self, ammo_type):
        self.image = self.ammo_list[ammo_type].image
        self.rect = self.image.get_rect()
        self.sound = self.ammo_list[ammo_type].sound
        self.speed = self.ammo_list[ammo_type].speed
        self.speed_increase = self.ammo_list[ammo_type].speed_increase

    def ammo_change(self):
        if self.ammo_active == self.AMMO_LASER:
            self.ammo_active = self.AMMO_TORPEDO
        else:
            self.ammo_active = self.AMMO_LASER

        self.image = self.ammo_list[self.ammo_active].image
        self.sound = self.ammo_list[self.ammo_active].sound
        self.speed = self.ammo_list[self.ammo_active].speed
        self.speed_increase = self.ammo_list[self.ammo_active].speed_increase

    def set_ready_status(self):
        self.status = self.STATUS_READY
        self.rect.y = -self.rect.height
        self.speed = self.ammo_list[self.ammo_active].speed

    def move(self):
        self.speed += self.speed * self.speed_increase
        self.rect.y -= self.speed

    def update(self):
        if self.rect.y > (-self.rect.height) and self.status == self.STATUS_FIRED:
            self.move()
        else:
            self.set_ready_status()
