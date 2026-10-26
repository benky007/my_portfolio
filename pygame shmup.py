#shmup
import pygame
import random
import time

#getting sizes and frames per second
WIDTH = 480
HEIGHT = 600
FPS = 60

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
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        '''
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -10
            print("here")
        if keystate[pygame.K_d]:
            self.speedx = 10
        '''
        #self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        #time.sleep(1)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.speedx = -8
                player.rect.x += player.speedx
            if event.key == pygame.K_d:
                player.speedx = 8
                player.rect.x += player.speedx
            
    #update
    all_sprites.update()
    
    #draw/render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #after drawing anything allways flip the display
    pygame.display.flip()

    player.speedx = 0

pygame.quit()
