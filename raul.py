import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
IMAGE_PLAYER = 'ico_ufo.png'
PLAYER_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        # super()._init_()
        super().__init__()
        self.image = pygame.image.load(IMAGE_PLAYER)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def right(self):
        self.rect.x += PLAYER_SPEED
    def left(self):
        self.rect.x -= PLAYER_SPEED
    def update(self):
        pass

if __name__ == '__main__':
    # General setup
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    # Game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Player
    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # Game loop
    running = True
    while running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left()
                elif event.key == pygame.K_RIGHT:
                    player.right()
        # Update
        screen.fill(pygame.Color(255, 255, 255))
        player_group.update()
        player_group.draw(screen)
        pygame.display.flip()
        # Clock
        clock.tick(fps)

        # print(player.rect.center)

    pygame.quit()
