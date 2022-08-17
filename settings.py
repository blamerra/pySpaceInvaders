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
        self.audio_background = "media/sound/background_sw_theme_song.mp3"
        self.audio_background_volume = 0.5

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
        self.player_sound_random = []
        self.player_sound_random.append("media/sound/player_sw_R2D2_sound0.wav")
        self.player_sound_random.append("media/sound/player_sw_R2D2_sound1.wav")
        self.player_sound_random.append("media/sound/player_sw_R2D2_sound2.wav")
        self.player_sound_random.append("media/sound/player_sw_R2D2_sound3.mp3")
        self.player_sound_random.append("media/sound/player_sw_R2D2_sound4.wav")
        self.player_sound_random.append("media/sound/player_sw_R2D2_sound5.wav")
        self.player_sound_random.append("media/sound/player_sw_R2D2_sound6.wav")

        self.player_sound_random0 = "media/sound/player_sw_R2D2_sound0.wav"
        self.player_sound_random1 = "media/sound/player_sw_R2D2_sound1.wav"
        self.player_sound_random2 = "media/sound/player_sw_R2D2_sound2.wav"
        self.player_sound_random3 = "media/sound/player_sw_R2D2_sound3.mp3"
        self.player_sound_random4 = "media/sound/player_sw_R2D2_sound4.wav"
        self.player_sound_random5 = "media/sound/player_sw_R2D2_sound5.wav"
        self.player_sound_random6 = "media/sound/player_sw_R2D2_sound6.wav"

        self.player_sound_random_probability = 0.003
        self.player_sound_random_volume = 0.7
        self.player_sound_random_delay = 1000  # miliseconds

        # Bullet settings
        self.bullet_image = "media/img/bullet_laser.png"
        self.bullet_sound = "media/sound/bullet_sw_blaster.wav"
        self.bullet_sound_volume = 0.5
        self.bullet_speed = 15
        self.shortcut_fire = pygame.K_SPACE

