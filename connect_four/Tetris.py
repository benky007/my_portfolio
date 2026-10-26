import pygame
import random

# getting sizes and frames per second
WIDTH = 360
HEIGHT = 480
FPS = 30

# getting colours so it is easier to call back
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Block:
    def __init__(self, color, width, height, shape):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

    def move(self, x=0, y=0):

    def pick_piece(self):

    def check_collisions(self):

    def check_lines(self):

    



# setting up the window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
object_ = Block(RED, 20, 30, 1)
object_.rect.x = 200
object_.rect.y = 300

all_sprites.add(object_)

# game loop
running = True
while running:
    # keep running at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update()

    # draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_a_tree(screen, 50, 100, 100)
    # after drawing anything allways flip the display
    pygame.display.flip()

pygame.quit()
