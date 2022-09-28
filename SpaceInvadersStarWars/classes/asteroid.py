import random
from pygame.transform import rotozoom

from .game_object import GameObject
from .utils import Utils
from settings import Settings


class Asteroid(GameObject):
    def __init__(self, position, create_asteroid_callback, size=3):
        self.size = size
        self.create_asteroid_callback = create_asteroid_callback
        size_to_scale = {
            3: 1.5,
            2: 0.75,
            1: 0.5,
        }
        self.sound_explosion = Utils.load_sound("explosion")

        self.scale = size_to_scale[size]
        sprite = rotozoom(Utils.load_sprite("asteroid"), 0, self.scale)

        super().__init__(
            position,
            sprite,
            Utils.get_random_velocity(Settings.ASTEROID_MIN_VELOCITY, Settings.ASTEROID_MAX_VELOCITY)
        )

        self.rotate_clockwise = bool(random.getrandbits(1))  # random bool
        self.MANEUVERABILITY = (abs(self.velocity[0]) + abs(self.velocity[1]))

    def draw(self, surface):
        self.rotate(self.rotate_clockwise)
        rotated_surface, blit_position = self.rotate_surface()
        surface.blit(rotated_surface, blit_position)

    def split(self):
        Utils.play_sound(self.sound_explosion)
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(
                    self.position, self.create_asteroid_callback, self.size - 1
                )
                self.create_asteroid_callback(asteroid)