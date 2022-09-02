import pygame
from settings import Settings
from classes.utils import Utils
from classes.game_object import GameObject
from classes.spaceship import Spaceship


class StarWars:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_icon(Utils.load_sprite("icon", False))

        self.background = Utils.load_sprite("background", False)
        self.clock = pygame.time.Clock()

        self.spaceship = Spaceship((400, 300))

    def run(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Star Wars")

    def _handle_input(self):
        # Gestion eventos KEYDOWN
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()



        # Gestion teclas pulsadas
        is_key_pressed = pygame.key.get_pressed()
        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate_forward()
            if is_key_pressed[pygame.K_DOWN]:
                self.spaceship.accelerate_back()
            if is_key_pressed[pygame.K_END]:
                self.spaceship.brake()
    def _process_game_logic(self):
        self.spaceship.move(self.screen)

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(Settings.fps)

