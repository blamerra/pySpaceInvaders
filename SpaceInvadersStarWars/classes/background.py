# Resources
# PyGame Beginner Tutorial in Python - Infinite Scrolling Background
# - https://www.youtube.com/watch?v=ARt6DLP38-Y
# - https://github.com/russs123/pygame_tutorials/blob/main/Infinite_Background/scroll_tut.py

from .game_object import GameObject
from .utils import Utils

class Background(GameObject):
    def __init__(self):
        super().__init__(
            (0, 0),
            Utils.load_sprite("background"),
            (0, 1)
        )
        self.scroll = 0


    def draw(self, surface):
        # surface.blit(self.sprite, blit_position)

        # draw scrolling background
        for i in range(0, 3):
            surface.blit(self.sprite, (0, i + self.sprite.get_height() + self.scroll, 0))

        # scroll background
        self.scroll -= 5

        # reset scroll
        if abs(self.scroll) > self.sprite.get_height():
            self.scroll = 0

