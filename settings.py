import pygame


class Settings:
    """A class to store all settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Game settings
        self.fps = 60
        self.shortcut_pause = pygame.K_PAUSE

        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.screen_icon = "media/img/ico.png"
        self.screen_title = "Space Invaders"

        # Audio
        self.audio_background = "media/sound/background.wav"

        # Background
        self.background_image = "media/img/background_scroll.png"
        self.background_scroll = True
        self.background_scroll_speed = 1
        self.shortcut_background_scroll_pause = pygame.K_b

        # Player settings
        self.player_image = "media/img/spaceship.png"
        self.player_image_x_margin = 5  # Margen en el eje x para que la nave no salga de la pantalla
        self.player_speed = 10
        self.player_vertical_move = True

        # Bullet settings
        self.bullet_image = "media/img/bullet_laser.png"
        self.bullet_speed = 12
        self.shortcut_fire = pygame.K_SPACE
        self.bullet_sound = "media/sound/bullet.wav"
