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


class Puck(pygame.sprite.Sprite):
    def __init__(self, color, blur, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        red1 = pygame.transform.scale(pygame.image.load("Red_puck-2.png").convert(), (width, height))
        red2 = pygame.transform.scale(pygame.image.load("Red_puck-3.png").convert(), (width, height))
        blue1 = pygame.transform.scale(pygame.image.load("Blue_puck-2.png").convert(), (width, height))
        blue2 = pygame.transform.scale(pygame.image.load("Blue_puck-3.png").convert(), (width, height))

        if color == "red":
            if blur:
                self.image.blit(red2, (0, 0))
            else:
                self.image.blit(red1, (0, 0))
        if color == "blue":
            if blur:
                self.image.blit(blue2, (0, 0))
            else:
                self.image.blit(blue1, (0, 0))
        self.rect = self.image.get_rect()


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

game_board = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]]

sprites = pygame.sprite.Group()

board = Board(20, 70, 2.5, 565, 490)
board.rect.x = 77
board.rect.y = 77

sprites.add(board)

temp = Puck("red", True, 70, 70)
temp.rect.x = 99.5
temp.rect.y = 7

sprites.add(temp)

done = False
clock = pygame.time.Clock()
count = 0
lock = [0, 0, 0, 0, 0, 0, 0]
current = 0

while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            done = True
        if pressed[pygame.K_ESCAPE]:
            done = True
        if pressed[pygame.K_RIGHT]:
            if current != 6:
                temp.rect.x += 75
                current += 1
            print(temp.rect.x)
        if pressed[pygame.K_LEFT]:
            if current - 1 == lock:
                if current - 2 >= 0:
                    temp.rect.x -= 75
                    current -= 1
                else:
                    pass
            elif current != 0:
                temp.rect.x -= 75
                current -= 1
            print(temp.rect.x)
        if pressed[pygame.K_RETURN]:
            if temp.rect.x == 99:
            if temp.rect.x == 174:
            if temp.rect.x == 249:
            if temp.rect.x == 324:
            if temp.rect.x == 399:
            if temp.rect.x == 474:
            if temp.rect.x == 549:

    for i in range(7):
        for row in game_board:
            if row[i] != 0:
                count += 1
        if count == 7:
            lock[i] = 1
        else:
            pass


    sprites.update()
    screen.fill(BLACK)
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.display.quit()
pygame.quit()
