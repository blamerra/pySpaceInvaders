from pygame.math import Vector2

from .game_object import GameObject
from .utils import Utils


class Bullet(GameObject):
    SPEED = 15

    def __init__(self, position, velocity, direction):
        super().__init__(
            position,
            Utils.load_sprite("bullet"),
            velocity
        )

        # Copia del objeto direction
        # sino se pasaria por refrencia y la bala rotaria con la nave
        self.direction = Vector2(direction)
        self.velocity = Vector2(velocity)

    def move(self, surface):
        self.position = self.position + self.direction * self.SPEED

    def draw(self, surface):
        rotated_surface, blit_position = self.rotate_surface()
        surface.blit(rotated_surface, blit_position)
