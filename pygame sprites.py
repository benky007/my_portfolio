#template
import pygame
import random
import os

#getting sizes and frames per second
WIDTH = 800
HEIGHT = 600
FPS = 30

#getting colours so it is easier to call back
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#setup assets
# game_folder = os.path.dirname(__file__)
# img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    #sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH /2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
        
#setting up the window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Adventures of Snom!!!")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
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
    screen.fill(BLUE)
    all_sprites.draw(screen)
    #after drawing anything allways flip the display
    pygame.display.flip()

pygame.quit()
