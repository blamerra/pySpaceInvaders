import pygame
# test git IDB Laptop
# Initialize game
pygame.init()
icon = pygame.image.load("media/img/ico.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Space Invaders")
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
screen = pygame.display.set_mode((800, 600))

# Game loop
running = 1
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
