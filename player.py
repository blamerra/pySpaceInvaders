
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT * 0.1)

    def move_up(self):
        if (self.rect.y > 0) & PLAYER_VERTICAL_MOVE:
            self.rect.y -= PLAYER_SPEED

    def move_down(self):
        if (self.rect.y < SCREEN_HEIGHT - self.rect.height) & PLAYER_VERTICAL_MOVE:
            self.rect.y += PLAYER_SPEED

    def move_right(self):
        if self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += PLAYER_SPEED

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            self.move_up()
        elif keys[pygame.K_DOWN]:
            self.move_down()