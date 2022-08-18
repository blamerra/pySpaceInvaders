import pygame
from settings import Settings
from sprites.audio import Audio
from sprites.background import Background
from sprites.frontend import Frontend
from sprites.bullet import Bullet
from sprites.player import Player
from sprites.fps import Fps


class Game:
    """Overall class to manage game assets and behavior."""
    SETTINGS = Settings()

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # Screen creation
        pygame.display.set_icon(pygame.image.load(self.SETTINGS.screen_icon))
        pygame.display.set_caption(self.SETTINGS.screen_title)
        self.screen = pygame.display.set_mode((self.SETTINGS.screen_width, self.SETTINGS.screen_height))

        # Fps
        self.clock = pygame.time.Clock()

        # Sprites creation
        self.audio = Audio()
        self.bullet = Bullet()
        self.background = Background()
        self.frontend = Frontend(self.screen)
        self.fps = Fps()
        self.player = Player()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.audio, self.background, self.bullet, self.player, self.fps, self.frontend)

        # Main loop running variables
        self.running = 1
        self.pause = 0

    def process_events(self):
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = 0

            if event.type == pygame.KEYDOWN:
                if event.key == self.SETTINGS.shortcut_pause:
                    self.pause = not self.pause
                if event.key == self.SETTINGS.shortcut_fire:
                    self.bullet.fire(self.player.rect.x, self.player.rect.y)

    def run_logic(self):
        pass

    def render_screen(self):
        # Render Screen
        if not self.pause:
            pygame.mixer.music.unpause()
            self.clock.tick(self.SETTINGS.fps)
            self.fps.set_fps(self.clock.get_fps())

            self.sprites.update()
            self.sprites.draw(self.screen)
            pygame.display.update()
        else:
            pygame.mixer.music.pause()

    def run(self):
        while self.running:
            self.process_events()
            self.run_logic()
            self.render_screen()
        pygame.quit()
