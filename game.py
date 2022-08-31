import pygame

from settings import Settings
from sprites.audio import Audio
from sprites.background import Background
from sprites.bullet import Bullet
from sprites.fps import Fps
from sprites.frontend import Frontend
from sprites.meteor import Meteor
from sprites.player import Player

class Game:
    """Overall class to manage game assets and behavior."""
    SETTINGS = Settings()

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.game_over = False
        self.score = 0

        # Screen creation
        pygame.display.set_icon(pygame.image.load(self.SETTINGS.screen_icon))
        pygame.display.set_caption(self.SETTINGS.screen_title)
        self.screen = pygame.display.set_mode((self.SETTINGS.screen_width, self.SETTINGS.screen_height))

        # Fps
        self.clock = pygame.time.Clock()

        # Sprites creation
        self.sprites = pygame.sprite.Group()

        self.audio = Audio()
        self.sprites.add(self.audio)

        self.background = Background()
        self.sprites.add(self.background)

        self.bullet = Bullet()
        self.sprites.add(self.bullet)

        self.player = Player()
        self.sprites.add(self.player)




        # Meteors
        # TODO refactor carga de imagenes en una clase

        meteor_image = pygame.image.load(self.SETTINGS.meteor_image).convert()
        self.meteor_list = pygame.sprite.Group()
        for i in range(self.SETTINGS.meteor_number):
            meteor = Meteor(meteor_image)
            self.sprites.add(meteor)
            self.meteor_list.add(meteor)

        # FPS
        self.fps = Fps()
        self.sprites.add(self.fps)

        # Animacion de la cortinilla de inicio
        self.frontend = Frontend(self.screen)
        self.sprites.add(self.frontend)

        # Main loop running variables
        self.running = 1
        self.pause = 0

    def process_events(self):
        # Event loop
        keys = pygame.key.get_pressed()
        if keys[self.SETTINGS.shortcut_fire]:
            self.bullet.fire(self.player.rect.x, self.player.rect.y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = 0
        '''
            if event.type == pygame.KEYDOWN:
                if event.key == self.SETTINGS.shortcut_pause:
                    self.pause = not self.pause
                # if event.key == self.SETTINGS.shortcut_fire:
                    # self.bullet.fire(self.player.rect.x, self.player.rect.y)
                  #   self.bullet.fire(300, 200)
        '''
        # Revisar si es necesario esta instruccion
        # pygame.event.pump()
    def run_logic(self):
        if not self.game_over:

            self.clock.tick(self.SETTINGS.fps)
            self.fps.set_fps(self.clock.get_fps())

            self.sprites.update()

            # Logica si el disparo ha destruido un meteoro
            if self.bullet.status == self.bullet.STATUS_FIRED:
                meteor_hit_list = pygame.sprite.spritecollide(self.bullet, self.meteor_list, True)
                if len(meteor_hit_list) > 0:
                    self.bullet.set_ready_status()
                    self.score += 1
                    print(self.score)

                if len(self.meteor_list) == 0:
                    print("GAME OVER - All meteors killed")
                    self.game_over = True

            # Logica si un meteoro ha colisionado con el player
            player_hit = pygame.sprite.spritecollide(self.player, self.meteor_list, True)
            if len(player_hit) > 0:
                pygame.mixer.music.stop()
                self.player.die()
                print("GAME OVER - Player died")
                self.game_over = True
    def render_screen(self):
        # self.screen.fill([0, 0, 0])

        # Render Screen
        if not self.pause:
            pygame.mixer.music.unpause()

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
