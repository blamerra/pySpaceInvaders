from pygame.math import Vector2
from pygame.transform import rotozoom

from .game_object import GameObject
from .utils import Utils


class Spaceship(GameObject):
    UP = Vector2(0, -1)
    MANEUVERABILITY = 3
    ACCELERATION = 0.25
    VELOCITY_MAX = 5

    def __init__(self, position):
        self.direction = Vector2(self.UP)
        super().__init__(position, Utils.load_sprite("spaceship"), Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(self.UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
    def _reset_max_velocity(self):
        if self.velocity[0] > self.VELOCITY_MAX:
            self.velocity[0] = self.VELOCITY_MAX
        if self.velocity[0] < -self.VELOCITY_MAX:
            self.velocity[0] = -self.VELOCITY_MAX
        if self.velocity[1] > self.VELOCITY_MAX:
            self.velocity[1] = self.VELOCITY_MAX
        if self.velocity[1] < -self.VELOCITY_MAX:
            self.velocity[1] = -self.VELOCITY_MAX

    def accelerate(self):
        self._reset_max_velocity()

        if self.VELOCITY_MAX >= self.velocity[0] >= -self.VELOCITY_MAX and self.VELOCITY_MAX >= self.velocity[1] >= -self.VELOCITY_MAX:
            self.velocity += self.direction * self.ACCELERATION

        print(self.velocity)

    def decelerate(self):
        self._reset_max_velocity()
        if self.VELOCITY_MAX >= self.velocity[0] >= -self.VELOCITY_MAX and self.VELOCITY_MAX >= self.velocity[1] >= -self.VELOCITY_MAX:
            self.velocity -= self.direction * self.ACCELERATION
        print(self.velocity)
