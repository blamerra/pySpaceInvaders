# Sprite usado para mostrar textos por la pantalla como la puntuacion
# Fuente: https://gist.github.com/Informatic/91bee5cfb71d4c7a3c2b

import pygame

class RenderText(pygame.sprite.Sprite):
    pos = None
    pos_rel = None

    def __init__(self, screen, text='text', pos=(0, 0),
                 font=None, size=20, color=(255, 255, 255), antialias=True):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.text = text
        self.position = pos
        self.screen = screen
        self.antialias = antialias

    def move(self, surface):
        pass

    def update(self):
        pass

    def print_text(self, text):
        self.text = text

    def draw(self, surface):
        self.image = self.font.render(self.text, self.antialias, self.color)
        surface.blit(self.image, self.position)