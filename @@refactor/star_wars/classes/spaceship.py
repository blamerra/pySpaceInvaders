from pygame.math import Vector2

from .bullet import Bullet
from .game_object import GameObject
from .utils import Utils


class Spaceship(GameObject):
    STOP = Vector2(0, 0)
    ACCELERATION = 0.25
    VELOCITY_MAX = 10
    DIRECTION_FORWARD = 1
    DIRECTION_BACK = -1
    BULLET_SPEED = 3

    def __init__(self, position, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback
        self.laser_sound = Utils.load_sound("bullet_laser")

        self.direction = Vector2(self.UP)
        super().__init__(position, Utils.load_sprite("spaceship"), Vector2(0))

    def draw(self, surface):
        self._reset_max_velocity()
        rotated_surface, blit_position = self.rotate_surface()
        surface.blit(rotated_surface, blit_position)

    # hay que hacer este reset ya que a veces se pasa por poco de la velocidad
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

    def accelerate_back(self):
        if self.VELOCITY_MAX >= self.velocity[0] >= -self.VELOCITY_MAX \
                and self.VELOCITY_MAX >= self.velocity[1] >= -self.VELOCITY_MAX:
            self.velocity -= self.direction * self.ACCELERATION

    def brake(self):
        self.velocity[0] = 0
        if self.velocity[1] < 0:
            self.accelerate_back()
        elif self.velocity[1] > 0:
            self.accelerate_forward()

        '''

        else:
            self.direction = self.UP

        if self.direction != self.UP:
            self.velocity[0] = 0
            if self.direction[0] > 0:
                self.rotate(False)
            if self.direction[0] < 0:
                self.rotate()
        '''
    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity, self.direction)
        self.create_bullet_callback(bullet)
        self.laser_sound.play()
