import random
from pygame.math import Vector2
from pygame.time import Clock
import pygame

from .bullet import Bullet
from .game_object import GameObject
from .utils import Utils
from settings import Settings

class Spaceship(GameObject):
    STOP = Vector2(0, 0)
    ACCELERATION = 1
    VELOCITY_MAX = 10
    DIRECTION_FORWARD = 1
    DIRECTION_BACK = -1
    BULLET_SPEED = 3
    RANDOM_SOUNDS_NUMBER = 6
    def __init__(self, position, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback
        self.laser_sound = Utils.load_sound("bullet_laser")
        self.random_sounds = []

        self.direction = Vector2(self.UP)
        super().__init__(position, Utils.load_sprite("spaceship"), Vector2(0))

        self.clock = Clock()
        self.random_sounds_time_elapsed = 0
        self.RANDOM_SOUNDS_DELAY = Settings.SPACESHIP_RANDOM_SOUND_DELAY

        self.random_sounds = []
        for i in range(self.RANDOM_SOUNDS_NUMBER):
            self.random_sounds.append(Utils.load_sound(f'starship_R2D2_sound{i}'))

        self.sound_accelerate = Utils.load_sound("starship_accelerate", "flac")
        self.sound_accelerate.set_volume(0.3)
        self.sound_accelerate_channel = pygame.mixer.find_channel()
        self.sound_accelerate_backward = Utils.load_sound("starship_accelerate_backward", "wav")
        self.sound_accelerate_brake = Utils.load_sound("starship_accelerate_brake", "wav")
        #self.sound_accelerate_brake.set_volume(0.3)

    def draw(self, surface):
        self._reset_max_velocity()
        self._play_random_sound()
        rotated_surface, blit_position = self.rotate_surface()
        surface.blit(rotated_surface, blit_position)

    def _play_random_sound(self):
        # the following method returns the time since its last call in milliseconds
        # it is good practice to store it in a variable called 'dt'
        dt = self.clock.tick()
        self.random_sounds_time_elapsed += dt
        if self.random_sounds_time_elapsed > self.RANDOM_SOUNDS_DELAY:
            print(self.random_sounds_time_elapsed)
            self.random_sounds[random.randrange(0, self.RANDOM_SOUNDS_NUMBER)].play()
            self.random_sounds_time_elapsed = 0  # reset it to 0 so you can count again


    # hay que hacer este reset ya que a veces se pasa por poco de la velocidad maxima/minima
    def _reset_max_velocity(self):
        if self.velocity[0] > self.VELOCITY_MAX:
            self.velocity[0] = self.VELOCITY_MAX
        if self.velocity[0] < -self.VELOCITY_MAX:
            self.velocity[0] = -self.VELOCITY_MAX
        if self.velocity[1] > self.VELOCITY_MAX:
            self.velocity[1] = self.VELOCITY_MAX
        if self.velocity[1] < -self.VELOCITY_MAX:
            self.velocity[1] = -self.VELOCITY_MAX

    def accelerate_forward(self):
        if self.VELOCITY_MAX >= self.velocity[0] >= -self.VELOCITY_MAX \
                and self.VELOCITY_MAX >= self.velocity[1] >= -self.VELOCITY_MAX:
            self.velocity += self.direction * self.ACCELERATION
            Utils.play_sound(self.sound_accelerate, self.sound_accelerate_channel)

    def accelerate_back(self):
        self.velocity = self.velocity * 0.8
        Utils.play_sound(self.sound_accelerate_backward, self.sound_accelerate_channel)

        '''
        if self.VELOCITY_MAX >= self.velocity[0] >= -self.VELOCITY_MAX \
                and self.VELOCITY_MAX >= self.velocity[1] >= -self.VELOCITY_MAX:
            self.velocity -= self.direction * self.ACCELERATION
            Utils.play_sound(self.sound_accelerate_backward, self.sound_accelerate_channel)
        '''
    def brake(self):
        Utils.play_sound(self.sound_accelerate_brake, self.sound_accelerate_channel)
        self.velocity = self.velocity * 0.3

    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity, self.direction)
        self.create_bullet_callback(bullet)
        Utils.play_sound(self.laser_sound)

