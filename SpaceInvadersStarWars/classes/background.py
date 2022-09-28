# Resources
# PyGame Beginner Tutorial in Python - Infinite Scrolling Background
# - https://www.youtube.com/watch?v=ARt6DLP38-Y
# - https://github.com/russs123/pygame_tutorials/blob/main/Infinite_Background/scroll_tut.py
import math
from .game_object import GameObject
from .utils import Utils

class Background(GameObject):
    def __init__(self, velocity, screen_width, screen_height):
        super().__init__(
            (0, 0),
            Utils.load_sprite("background"),
            velocity
        )

        # define scrolling background
        self.bg_width = self.sprite.get_width()
        self.bg_height = self.sprite.get_height()
        self.bg_scroll = 0
        self.bg_tiles = math.ceil(screen_height / screen_width) + 1

    def draw(self, surface):
        # surface.blit(self.sprite, blit_position)

        # draw scrolling background
        for i in range(0, self.bg_tiles):
            surface.blit(self.sprite, (0, -i * self.bg_height + self.bg_scroll))

        # scroll background
        self.bg_scroll += self.velocity.y

        # reset scroll
        if abs(self.bg_scroll) > self.bg_height:
            self.bg_scroll = 0
