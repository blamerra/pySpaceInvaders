import pygame
from settings import Settings
from sprites.background import Background
from sprites.player import Player
from sprites.fps import Fps


class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Screen creation
        pygame.display.set_icon(pygame.image.load(self.settings.screen_icon))
        pygame.display.set_caption(self.settings.screen_title)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.clock = pygame.time.Clock()

        # Sprites creation
        self.player = Player()
        self.background = Background()
        self.fps = Fps()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.background, self.player, self.fps)

        self.running = 1
        self.pause = 0

    def process_events(self):
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = 0

            if event.type == pygame.KEYDOWN:
                if event.key == self.settings.shortcut_pause:
                    self.pause = not self.pause
                if event.key == self.settings.shortcut_background_scroll_pause:
                    self.background.pause()

    def run_logic(self):
        pass

    def render_screen(self):
        # Render Screen
        if not self.pause:
            self.clock.tick(self.settings.fps)
            self.fps.fps = str(int(self.clock.get_fps()))

            self.sprites.update()
            self.sprites.draw(self.screen)
            pygame.display.update()

    def run(self):
        while self.running:
            self.process_events()
            self.run_logic()
            self.render_screen()
        pygame.quit()
