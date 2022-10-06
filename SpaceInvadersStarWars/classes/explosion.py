from pygame.transform import rotozoom
from .game_object import GameObject
from .utils import Utils


class Explosion(GameObject):
    def __init__(self, position, scale=1, delete_explosion_callback=None):
        self.delete_explosion_callback = delete_explosion_callback
        #num_images = 7
        # se multiplica la escala por 0.75 ya que la explosion tiene 80px en lugar de 64
        #scale_adjustment = 0.75

        num_images = 9
        # se multiplica la escala por 0.42 ya que la explosion tiene 150px en lugar de 64
        scale_adjustment = 0.42
        
        self.images = []
        for num in range(0, num_images):
            #img = Utils.load_sprite(f"explosion0{num}")
            img = Utils.load_sprite(f"regularExplosion0{num}")
            img = rotozoom(img, 0, scale * scale_adjustment)
            self.images.append(img)

        self.index = 0
        self.counter = 0

        self.sound = Utils.load_sound("explosion")
        Utils.play_sound(self.sound, 0.5)

        super().__init__(
            position,
            self.images[self.index],
            (0, 0)
        )

    def draw(self, surface):
        explosion_speed = 3
        # update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images)-1:
            self.counter = 0
            self.index += 1
            self.sprite = self.images[self.index]

        # if the animation is complete, reset animation index
        if self.index >= len(self.images) and self.counter >= explosion_speed:
            self.sprite = self.images[0]  # la ultima animacion esta en blanco
            self.delete_explosion_callback

        super().draw(surface)
        # surface.blit(self.sprite, self.position)
