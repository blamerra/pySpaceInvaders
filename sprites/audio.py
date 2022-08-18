import pygame
from random import random
from settings import Settings


class Audio(pygame.sprite.Sprite):
    SETTINGS = Settings()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1, 1))
        self.rect = self.image.get_rect()

        # Channels settings
        pygame.mixer.set_num_channels(20)

        # Background music
        pygame.mixer.music.load(self.SETTINGS.audio_background)
        pygame.mixer.music.set_volume(self.SETTINGS.audio_background_volume)
        pygame.mixer.music.play(-1)

        # Random sounds
        self.sound_index = 0
        self.sound_last_play_time = 0
        self.sound_delay = self.SETTINGS.player_sound_random_delay
        self.sounds = self.SETTINGS.player_sound_random.copy()
        self.current_sound = pygame.mixer.Sound(self.sounds[self.sound_index])

    def play_random_sound(self):
        play_sound = True if random() < self.SETTINGS.player_sound_random_probability else False

        if play_sound and ((pygame.time.get_ticks() - self.sound_last_play_time) > self.sound_delay):
            print("SOUND: " + str(self.sound_index))

            self.current_sound.stop()
            self.current_sound = pygame.mixer.Sound(self.sounds[self.sound_index])
            self.current_sound.set_volume(self.SETTINGS.player_sound_random_volume)
            pygame.mixer.find_channel().play(self.current_sound)

            if self.sound_index < len(self.sounds)-1:
                self.sound_index += 1
            else:
                self.sound_index = 0

    def update(self):
        self.play_random_sound()