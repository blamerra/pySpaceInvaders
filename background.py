import pygame
from settings import Settings


class Background(pygame.sprite.Sprite):
    settings = Settings()

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(self.settings.background_image).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, -self.settings.screen_height]
        self.scroll = self.settings.background_scroll
        self.scroll_speed = self.settings.background_scroll_speed

    def update(self):
        # keys = pygame.key.get_pressed()
        # if keys[SHORTCUT_BACKGROUND_SCROLL_STOP]:
        #    self.scroll = not self.scroll

        if self.scroll:
            if self.rect.y < 0:
                self.rect.y += self.scroll_speed
            else:
                self.rect.y = -self.settings.screen_height

    def pause(self):
        self.scroll = not self.scroll
