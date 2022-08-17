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

        self.sound_index = 0
        self.sound_last_play_time = 0
        self.sounds = self.SETTINGS.player_sound_random.copy()
        '''
        self.sound.append(pygame.mixer.Sound(self.SETTINGS.player_sound_random0))
        self.sound[0].set_volume(self.SETTINGS.player_sound_random_volume)
        self.sound.append(pygame.mixer.Sound(self.SETTINGS.player_sound_random1))
        self.sound[1].set_volume(self.SETTINGS.player_sound_random_volume)
        self.sound.append(pygame.mixer.Sound(self.SETTINGS.player_sound_random2))
        self.sound[2].set_volume(self.SETTINGS.player_sound_random_volume)
        self.sound.append(pygame.mixer.Sound(self.SETTINGS.player_sound_random3))
        self.sound[3].set_volume(self.SETTINGS.player_sound_random_volume)
        '''
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

    def play_random_sound(self):
        play_sound = True if random() < self.SETTINGS.player_sound_random_probability else False

        if ((pygame.time.get_ticks() - self.sound_last_play_time) > self.SETTINGS.player_sound_random_delay) and play_sound:
            print("SOUND: " + str(self.sound_index))

            sound = pygame.mixer.Sound(self.sounds[self.sound_index])
            sound.set_volume(self.SETTINGS.player_sound_random_volume)
            pygame.mixer.find_channel().play(sound)

            # self.sound[0].set_volume(self.SETTINGS.player_sound_random_volume)
            # pygame.mixer.find_channel().play(self.sound[self.sound_index])

            if self.sound_index < len(self.sounds)-1:
                self.sound_index += 1
            else:
                self.sound_index = 0

    def update(self):
        self.play_random_sound()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()
