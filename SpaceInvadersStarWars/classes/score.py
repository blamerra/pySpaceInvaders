import pygame
from pygame.math import Vector2
from pygame import Color
from .game_object import GameObject
from .utils import Utils


class Score(GameObject):
    score = 0

    def __init__(self, screen_width, screen_height):
        position = (screen_width - 100, screen_height + 15)
        position = (10, 10)
        color = Color("gold1")
        self.font = self.font = pygame.font.Font(None, 64)

        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.font.render(self._getDisplayText(), True, color)
        self.sprite.rect = self.sprite.image.get_rect()

        #pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))

        self.position = Vector2(position)
        self.velocity = Vector2(0,0)



        #self.image = self.font.render(self._getDisplayText(), True, color)
        #self.rect = self.image.get_rect()

        #surface = self.font.render(self._getDisplayText(), True, color)

        #rect = text_surface.get_rect()
        #rect.center = Vector2(surface.get_size()) / 2

        #surface.blit(text_surface, rect)

    def _getDisplayText(self):
        return "score : " + str(self.score)

    def increase(self):
        self.score += 1

    def draw(self, surface):

        color = Color("gold1")
        self.sprite.image = self.font.render(self._getDisplayText(), True, color)

        self.sprite.image.rect = self.sprite.image.get_rect()
        self.sprite.rect.center = Vector2(surface.get_size()) / 2

        surface.blit(self.sprite.image, self.sprite.rect)

    #Utils.print_text(surface, "score : " + str(self.score), self.font)
