import pygame
from pygame.transform import rotozoom
from settings import Settings
from classes.utils import Utils
from classes.spaceship import Spaceship
from classes.asteroid import Asteroid


class StarWars:
    def _create_asteroids(self):
        # Aseguramos que hay un minimo de de distancia entre la nave y los asteroides
        for _ in range(Settings.ASTEROID_NUMBER):
            while True:
                position = Utils.get_random_position(self.screen)
                if position.distance_to(self.spaceship.position) > Settings.ASTEROID_MIN_DISTANCE:
                    break

            self.asteroids.append(Asteroid(position, self.asteroids.append))

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Star Wars")
        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        pygame.display.set_icon(Utils.load_sprite("icon", False))

        # self.background = Utils.load_sprite("background", False)
        self.background = rotozoom(Utils.load_sprite("background"), 0, 2)
        self.clock = pygame.time.Clock()

        # Music
        Utils.load_background_sound("background_sw_theme_song.mp3")

        # Sprites
        self.bullets = []

        self.spaceship = Spaceship(
            Utils.get_center_position(self.screen, 0, 150),
            self.bullets.append
        )

        self.asteroids = []
        self._create_asteroids()

        self.font = pygame.font.Font(None, 64)
        self.message = ""

    def run(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _handle_input(self):
        # Gestion eventos KEYDOWN
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
            elif self.spaceship and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.spaceship.shoot()
                #elif event.key == pygame.K_UP:
                #    self.spaceship.accelerate_forward()
                elif event.key == pygame.K_DOWN:
                    self.spaceship.accelerate_back()
                elif event.key == pygame.K_END:
                    self.spaceship.brake()

            # custom timer events
            elif event.type == pygame.USEREVENT+1:
                # spaceship kill
                self.spaceship = None

        # Gestion teclas pulsadas
        is_key_pressed = pygame.key.get_pressed()
        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            elif is_key_pressed[pygame.K_UP]:
                    self.spaceship.accelerate_forward()
            '''
            elif is_key_pressed[pygame.K_END]:
                self.spaceship.brake()
               
            elif is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate_forward()
            elif is_key_pressed[pygame.K_DOWN]:
                self.spaceship.accelerate_back()
'''


    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]
        if self.spaceship:
            game_objects.append(self.spaceship)

        return game_objects

    def _process_game_logic_spaceship(self):
        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship.die()
                    # self.spaceship = None
                    self.message = "You lost!"
                    Utils.load_background_sound("background_sw_imperial_march.mp3")
                    pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
                    break

    def _process_game_logic_bullet(self):
        # Bullet logic
        # Notice that instead  of using the original list, self.bullets,
        # you create a copy of it using self.bullets[:]
        # That’s because removing elements from a list while iterating over it can cause errors.

        # control si la bala sale de la pantalla
        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)

        # control si la bala choca con un asteroide
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    break

    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        self._process_game_logic_spaceship()
        self._process_game_logic_bullet()

        if not self.asteroids and self.spaceship:
            # TODO arreglar que no se recargue todo el rato con una variable
            #  game_status
            self.message = "You won!"
            Utils.load_background_sound("background_sw_rebel_theme.mp3")

    def _draw(self):
        self.screen.blit(self.background, (0, 0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        if self.message:
            Utils.print_text(self.screen, self.message, self.font)

        pygame.display.flip()
        self.clock.tick(Settings.FPS)