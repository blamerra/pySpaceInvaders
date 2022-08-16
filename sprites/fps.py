import pygame
from settings import Settings


class Fps(pygame.sprite.Sprite):
    settings = Settings()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (self.settings.screen_width - 10, 10)
        self.font = pygame.font.SysFont("Arial", 18)
        self.fps = None
        self.fps_text = None

    def update(self):
        self.image.fill(pygame.Color("black"))
        self.fps_text = self.font.render(self.fps, True, pygame.Color("coral"))
        self.image.blit(self.fps_text, [0, 0])
