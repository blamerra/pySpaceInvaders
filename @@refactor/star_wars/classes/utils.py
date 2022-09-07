import random
from pygame.image import load
from pygame.mixer import Sound
from pygame.math import Vector2


class Utils:
    @staticmethod
    def load_sprite(name, with_alpha=True):
        path = f"assets/images/{name}.png"
        loaded_sprite = load(path)

        if with_alpha:
            return loaded_sprite.convert_alpha()
        else:
            return loaded_sprite.convert()

    @staticmethod
    def load_sound(name, extension="wav"):
        path = f"assets/sounds/{name}.{extension}"
        return Sound(path)

    # Position functions
    @staticmethod
    def wrap_position(position, surface):
        x, y = position
        w, h = surface.get_size()
        return Vector2(x % w, y % h)

        '''
        # Opcion para que el limite fijo este en los bordes y se pare
        return_x = max(32, min(x, w-32))
        return_y = max(32, min(y, h-32))
        return_vector = Vector2(return_x, return_y)
        return return_vector
        '''

    @staticmethod
    def get_random_position(surface):
        return Vector2(
            random.randrange(surface.get_width()),
            random.randrange(surface.get_height()),
        )

    @staticmethod
    def get_center_position(surface):
        return Vector2(
            surface.get_width()/2,
            surface.get_height()/2
        )

    @staticmethod
    def get_random_velocity(min_speed, max_speed):
        speed = random.randint(min_speed, max_speed)
        angle = random.randrange(0, 360)
        return Vector2(speed, 0).rotate(angle)
