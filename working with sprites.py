import pygame
import random
import os



WIDTH = 360 # width of game window
HEIGHT = 480 # height of screen
FPS = 30 # frames

#COLORS (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#classes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x +=5

        if self.rect.left> WIDTH:
            self.rect.right =0



pygame.init()
pygame.mixer.init() # for sound
screen= pygame.display.set_mode((WIDTH, HEIGHT))

# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert()


pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player= Player()
all_sprites.add(player)

# Game Loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update()

    # render (draw)

    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
