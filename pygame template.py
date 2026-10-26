#template
import pygame
import random

#getting sizes and frames per second
WIDTH = 360
HEIGHT = 480
FPS = 30

#getting colours so it is easier to call back
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#setting up the window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
#game loop
running = True
while running:
    #keep running at the right speed
    clock.tick(FPS)
    #process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
            
    #update
    all_sprites.update()
    
    #draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #after drawing anything allways flip the display
    pygame.display.flip()

pygame.quit()
