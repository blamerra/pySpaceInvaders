import pygame


class Ammo:
    def __init__(self, name, image, sound, sound_volume, speed, speed_increase):
        self.name = name
        self.image = pygame.image.load(image).convert_alpha()
        self.sound = pygame.mixer.Sound(sound)
        self.sound.set_volume(sound_volume)
        self.speed = speed
        self.speed_increase = speed_increase
