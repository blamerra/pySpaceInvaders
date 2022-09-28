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
    ACCELERATION = 0.2
    VELOCITY_MAX = 10
    DIRECTION_FORWARD = 1
    DIRECTION_BACK = -1
    BULLET_SPEED = 3
    RANDOM_SOUNDS_NUMBER = 6

    def __init__(self, position, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback
        self.is_alive = True

        self.random_sounds = []

        self.direction = Vector2(self.UP)
        self.sprite_spaceship = Utils.load_sprite("spaceship")
        self.sprite_spaceship_forward = Utils.load_sprite("spaceship_forward")
        self.sprite_spaceship_backward = Utils.load_sprite("spaceship_backward")
        self.sprite_spaceship_explosion = Utils.load_sprite("spaceship_explosion")
        self.sprite_spaceship_die = Utils.load_sprite("spaceship_die")
        super().__init__(position, self.sprite_spaceship, Vector2(0))

        self.velocity = Vector2(0, -1)
        self.clock = Clock()
        self.random_sounds_time_elapsed = 0
        self.RANDOM_SOUNDS_DELAY = Settings.SPACESHIP_RANDOM_SOUND_DELAY

        self.random_sounds = []
        for i in range(self.RANDOM_SOUNDS_NUMBER):
            self.random_sounds.append(Utils.load_sound(f'starship_R2D2_sound{i}'))

        self.sound_accelerate = Utils.load_sound("starship_accelerate_forward", "flac")
        self.sound_accelerate.set_volume(0.3)
        self.sound_accelerate_channel = pygame.mixer.find_channel()
        self.sound_accelerate_backward = Utils.load_sound("starship_accelerate_backward", "wav")
        self.sound_accelerate_brake = Utils.load_sound("starship_accelerate_brake", "wav")
        # self.sound_accelerate_brake.set_volume(0.3)

        self.sound_kill = Utils.load_sound("explosion")

        self.acceleration_time_elapsed = 0
        self.ACCELERATION_DELAY = 500

    def draw(self, surface):
        if self.is_alive:
            self._reset_max_velocity()
            self._reset_animation_motors()
            self._play_random_sound()

        rotated_surface, blit_position = self.rotate_surface()
        surface.blit(rotated_surface, blit_position)

    def _play_random_sound(self):
        if self.is_alive:
            # the following method returns the time since its last call in milliseconds
            # it is good practice to store it in a variable called 'dt'
            dt = self.clock.tick()
            self.random_sounds_time_elapsed += dt
            if self.random_sounds_time_elapsed > self.RANDOM_SOUNDS_DELAY:
                self.random_sounds[random.randrange(0, self.RANDOM_SOUNDS_NUMBER)].play()
                self.random_sounds_time_elapsed = 0  # reset it to 0 so you can count again

    def _reset_animation_motors(self):
        if self.is_alive:
            # Reset motor image after some time without acceleration
            dt = self.clock.tick()
            self.acceleration_time_elapsed += dt
            if self.acceleration_time_elapsed > self.ACCELERATION_DELAY:
                self.sprite = self.sprite_spaceship
                self.acceleration_time_elapsed = 0

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
        if self.is_alive:
            if self.VELOCITY_MAX >= self.velocity[0] >= -self.VELOCITY_MAX \
                    and self.VELOCITY_MAX >= self.velocity[1] >= -self.VELOCITY_MAX:
                self.velocity += self.direction * self.ACCELERATION
                Utils.play_sound(self.sound_accelerate, 1, self.sound_accelerate_channel)
                self.sprite = self.sprite_spaceship_forward

    def accelerate_back(self):
        if self.is_alive:
            self.velocity = self.velocity * 0.8
            Utils.play_sound(self.sound_accelerate_backward, 1, self.sound_accelerate_channel)
            self.sprite = self.sprite_spaceship_backward

        '''
        if self.VELOCITY_MAX >= self.velocity[0] >= -self.VELOCITY_MAX 
                and self.VELOCITY_MAX >= self.velocity[1] >= -self.VELOCITY_MAX:
            self.velocity -= self.direction * self.ACCELERATION
            Utils.play_sound(self.sound_accelerate_backward, self.sound_accelerate_channel)
        '''

    def brake(self):
        Utils.play_sound(self.sound_accelerate_brake, 1, self.sound_accelerate_channel)
        self.velocity = self.velocity * 0.3

    def shoot(self):
        if self.is_alive:
            bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
            bullet = Bullet(self.position, bullet_velocity, self.direction)
            self.create_bullet_callback(bullet)

    def die(self):
        if self.is_alive:
            #Utils.play_sound(self.sound_kill)
            self.velocity = self.STOP
            self.sprite = self.sprite_spaceship_die
            self.is_alive = False

    def rotate(self, clockwise=True):
        if self.is_alive:
            super().rotate(clockwise)
