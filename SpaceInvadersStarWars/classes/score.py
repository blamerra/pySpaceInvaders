import pygame
from pygame.math import Vector2
from pygame import Color
from .render_text import RenderText
from .utils import Utils


class Score(RenderText):
    score = 0

    def __init__(self, screen, screen_width, screen_height):
        self.score = 0

        super().__init__(
            screen,
            self._get_display_text(),
            size=25,
            pos=[screen_width - 90, 10],
            color=Color("gold1")
        )

    def _get_display_text(self):
        return "score : " + str(self.score)

    def increase(self):
        self.score += 1
        self.set_text(self._get_display_text())
