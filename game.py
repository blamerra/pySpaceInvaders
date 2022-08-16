import pygame
from settings import Settings
from background import Background
from player import Player
from fps import Fps


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

        # Sprites creation
        self.player = Player()
        self.background = Background()
        self.fps = Fps()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.background, self.player, self.fps)

    def run(self):
        running = 1
        pause = 0
        while running:

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == self.settings.shortcut_pause:
                        pause = not pause
                    if event.key == self.settings.shortcut_background_scroll_pause:
                        self.background.pause()

            # Render Screen
            if not pause:
                self.sprites.update()
                self.sprites.draw(self.screen)
                pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run()
