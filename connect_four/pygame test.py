import pygame
import math
import time

WIDTH = 720
HEIGHT = 645
FPS = 300

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Board(pygame.sprite.Sprite):
    def __init__(self, rnd, place, place_bd, width, height):
        super().__init__()
        self.master = pygame

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        self.master.draw.line(self.image, RED, (0, height / 2),
                              (width, height / 2),
                              width=height)
        self.master.draw.circle(self.image, BLACK, (0, 0), rnd)
        self.master.draw.circle(self.image, RED, (rnd, rnd + 1), rnd)
        self.master.draw.circle(self.image, BLACK, (width, height), rnd)
        self.master.draw.circle(self.image, RED, (width - rnd + 1, height - rnd),
                                rnd)
        self.master.draw.circle(self.image, BLACK, (width, 0), rnd)
        self.master.draw.circle(self.image, RED, (width - rnd + 1, rnd + 1), rnd)
        self.master.draw.circle(self.image, BLACK, (0, height), rnd)
        self.master.draw.circle(self.image, RED, (rnd, height - rnd), rnd)

        self.master.draw.line(self.image, WHITE, (rnd, 1+rnd), (rnd, height-1-rnd), width=1)
        self.master.draw.line(self.image, WHITE, (width - rnd, rnd),
                              (width - rnd, height-rnd), width=1)
        self.calculate(self.master, self.image, 90, rnd, rnd, width - 2*rnd, WHITE, 1)
        self.calculate(self.master, self.image, 90, rnd, height - rnd, width - 2*rnd, WHITE, 1)
        for i in range(1, 6):
            self.calculate(self.master, self.image, 90, rnd + 1, rnd + (((height - 2*rnd) / 6) * i), width - 2*rnd - 1,
                           WHITE, 1)
        for i in range(1, 7):
            self.calculate(self.master, self.image, 180, rnd + (((width - 2*rnd) / 7) * i), 1 + rnd, height - 1 - rnd*2,
                           WHITE, 1)

        y_co = rnd + 1.25 + place_bd + place / 2
        for y_ in range(1, 7):
            x_co = rnd + 1.25 + place_bd + place / 2
            if y_ != 1:
                y_co += 2 * place_bd + 2 * (place / 2)
            for x_ in range(1, 8):
                if x_ != 1:
                    x_co += 2 * place_bd + 2 * (place / 2)
                self.master.draw.circle(self.image, BLACK, (x_co, y_co), place/2)

        self.rect = self.image.get_rect()

    @staticmethod
    def calculate(master, surface, angle, start_x, start_y, length, colour, width):
        while not 0 <= angle <= 360:
            if angle < 0:
                angle += 360
            if angle > 360:
                angle -= 360
        if angle == 0:
            master.draw.line(surface, colour, (start_x, start_y), (start_x, start_y - length), width=width)
        if 0 < angle < 90:
            adjacent = math.cos(math.radians(angle)) * length
            opposite = math.sin(math.radians(angle)) * length
            # print("hypotenuse: ", length, "\nadjacent: ", adjacent, "\nopposite", opposite)
            master.draw.line(surface, colour, (start_x, start_y), (start_x + opposite, start_y - adjacent),
                             width=width)
        if angle == 90:
            master.draw.line(surface, colour, (start_x, start_y), (start_x + length, start_y),
                             width=width)
        if 90 < angle < 180:
            adjacent = math.cos(math.radians(angle - 90)) * length
            opposite = math.sin(math.radians(angle - 90)) * length
            # print("hypotenuse: ", length, "\nadjacent: ", adjacent, "\nopposite", opposite)
            master.draw.line(surface, colour, (start_x, start_y), (start_x + adjacent, start_y + opposite),
                             width=width)
        if angle == 180:
            master.draw.line(surface, colour, (start_x, start_y), (start_x, start_y + length),
                             width=width)
        if 180 < angle < 270:
            adjacent = math.cos(math.radians(angle - 180)) * length
            opposite = math.sin(math.radians(angle - 180)) * length
            # print("hypotenuse: ", length, "\nadjacent: ", adjacent, "\nopposite", opposite)
            master.draw.line(surface, colour, (start_x, start_y), (start_x - opposite, start_y + adjacent),
                             width=width)
        if angle == 270:
            master.draw.line(surface, colour, (start_x, start_y), (start_x - length, start_y),
                             width=width)
        if 270 < angle < 360:
            adjacent = math.cos(math.radians(angle - 270)) * length
            opposite = math.sin(math.radians(angle - 270)) * length
            # print("hypotenuse: ", length, "\nadjacent: ", adjacent, "\nopposite", opposite)
            master.draw.line(surface, colour, (start_x, start_y), (start_x - adjacent, start_y - opposite),
                             width=width)
        if angle == 360:
            master.draw.line(surface, colour, (start_x, start_y), (start_x, start_y - length),
                             width=width)


pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")

all_sprites_list = pygame.sprite.Group()

object_ = Board(20, 70, 2.5, 565, 490)
object_.rect.x = 77
object_.rect.y = 77
x = 77
y = 77

all_sprites_list.add(object_)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            done = True
        if pressed[pygame.K_ESCAPE]:
            done = True
        if pressed[pygame.K_UP]:
            object_.rect.y -= 5
            y -= 5
        if pressed[pygame.K_DOWN]:
            object_.rect.y += 5
            y += 5
        if pressed[pygame.K_RIGHT]:
            object_.rect.x += 5
            x += 5
        if pressed[pygame.K_LEFT]:
            object_.rect.x -= 5
            x -= 5
        if pressed[pygame.K_RETURN]:
            object_ = Board(20, 70, 2.5, 565, 490)
            object_.rect.x = x
            object_.rect.y = y
            all_sprites_list.add(object_)

    all_sprites_list.update()
    screen.fill(BLACK)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
