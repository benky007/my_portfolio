import pygame
import random
import math
import time


class board:
    def __init__(self, master):
        self.master = master
        self.WIDTH = 720
        self.HEIGHT = 645
        self.FPS = 300

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        self.screen = self.master.display.set_mode((self.WIDTH, self.HEIGHT))
        self.master.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        time.sleep(1)
        self.draw_board()

    def draw_board(self):
        board_WIDTH = 565
        border_W = int((self.WIDTH - board_WIDTH) / 2)
        board_HEIGHT = 490
        border_H = int((self.HEIGHT - board_HEIGHT) / 2)
        rnd = 20
        place_bd = 2.5
        place = 70

        self.master.draw.line(self.screen, self.RED, (border_W, self.HEIGHT / 2),
                              (self.WIDTH - border_W, self.HEIGHT / 2),
                              width=board_HEIGHT)
        self.master.draw.circle(self.screen, self.BLACK, (border_W, border_H), rnd)
        self.master.draw.circle(self.screen, self.RED, (border_W + rnd, border_H + rnd + 1), rnd)
        self.master.draw.circle(self.screen, self.BLACK, (self.WIDTH - border_W, self.HEIGHT - border_H), rnd)
        self.master.draw.circle(self.screen, self.RED, (self.WIDTH - border_W - rnd + 1, self.HEIGHT - border_H - rnd),
                                rnd)
        self.master.draw.circle(self.screen, self.BLACK, (self.WIDTH - border_W, border_H), rnd)
        self.master.draw.circle(self.screen, self.RED, (self.WIDTH - border_W - rnd + 1, border_H + rnd + 1), rnd)
        self.master.draw.circle(self.screen, self.BLACK, (border_W, self.HEIGHT - border_H), rnd)
        self.master.draw.circle(self.screen, self.RED, (border_W + rnd, self.HEIGHT - border_H - rnd), rnd)

        self.master.draw.line(self.screen, self.WHITE, (border_W + rnd, border_H+1+rnd), (border_W + rnd, self.HEIGHT-border_H-1-rnd), width=1)
        self.master.draw.line(self.screen, self.WHITE, (self.WIDTH - border_W - rnd, border_H+rnd),
                              (self.WIDTH - border_W - rnd, self.HEIGHT-border_H-rnd), width=1)
        self.calculate(self.master, self.screen, 90, border_W + rnd, border_H + rnd, board_WIDTH - 2*rnd, self.WHITE, 1)
        self.calculate(self.master, self.screen, 90, border_W + rnd, self.HEIGHT - border_H - rnd, board_WIDTH - 2*rnd,
                       self.WHITE, 1)
        for i in range(1, 6):
            self.calculate(self.master, self.screen, 90, border_W + rnd + 1, border_H + rnd + (((board_HEIGHT - 2*rnd) / 6) * i),
                           board_WIDTH - 2*rnd - 1, self.WHITE, 1)
        for i in range(1, 7):
            self.calculate(self.master, self.screen, 180, border_W + rnd + (((board_WIDTH - 2*rnd) / 7) * i), border_H + 1 + rnd,
                           board_HEIGHT - 1 - rnd*2, self.WHITE, 1)

        y_co = border_H + rnd + 1.25 + place_bd + place / 2
        for y in range(1, 7):
            x_co = border_H + rnd + 1.25 + place_bd + place / 2
            if y != 1:
                y_co += 2 * place_bd + 2 * (place / 2)
            for x in range(1, 8):
                if x != 1:
                    x_co += 2 * place_bd + 2 * (place / 2)
                self.master.draw.circle(self.screen, self.BLACK, (x_co, y_co), place/2)

    @staticmethod
    def calculate(master, screen, angle, start_x, start_y, length, colour, width):
        while not 0 <= angle <= 360:
            if angle < 0:
                angle += 360
            if angle > 360:
                angle -= 360
        if angle == 0:
            master.draw.line(screen, colour, (start_x, start_y), (start_x, start_y - length), width=width)
        if 0 < angle < 90:
            adjacent = math.cos(math.radians(angle)) * length
            opposite = math.sin(math.radians(angle)) * length
            # print("hypotenuse: ", length, "\nadjacent: ", adjacent, "\nopposite", opposite)
            master.draw.line(screen, colour, (start_x, start_y), (start_x + opposite, start_y - adjacent),
                             width=width)
        if angle == 90:
            master.draw.line(screen, colour, (start_x, start_y), (start_x + length, start_y),
                             width=width)
        if 90 < angle < 180:
            adjacent = math.cos(math.radians(angle - 90)) * length
            opposite = math.sin(math.radians(angle - 90)) * length
            # print("hypotenuse: ", length, "\nadjacent: ", adjacent, "\nopposite", opposite)
            master.draw.line(screen, colour, (start_x, start_y), (start_x + adjacent, start_y + opposite),
                             width=width)
        if angle == 180:
            master.draw.line(screen, colour, (start_x, start_y), (start_x, start_y + length),
                             width=width)
        if 180 < angle < 270:
            adjacent = math.cos(math.radians(angle - 180)) * length
            opposite = math.sin(math.radians(angle - 180)) * length
            # print("hypotenuse: ", length, "\nadjacent: ", adjacent, "\nopposite", opposite)
            master.draw.line(screen, colour, (start_x, start_y), (start_x - opposite, start_y + adjacent),
                             width=width)
        if angle == 270:
            master.draw.line(screen, colour, (start_x, start_y), (start_x - length, start_y),
                             width=width)
        if 270 < angle < 360:
            adjacent = math.cos(math.radians(angle - 270)) * length
            opposite = math.sin(math.radians(angle - 270)) * length
            # print("hypotenuse: ", length, "\nadjacent: ", adjacent, "\nopposite", opposite)
            master.draw.line(screen, colour, (start_x, start_y), (start_x - adjacent, start_y - opposite),
                             width=width)
        if angle == 360:
            master.draw.line(screen, colour, (start_x, start_y), (start_x, start_y - length),
                             width=width)

    def start_game(self):
        done = False
        while not done:
            self.clock.tick(self.FPS)
            for event in self.master.event.get():
                try:
                    pressed = self.master.key.get_pressed()
                except pygame.error:
                    pass
                if event.type == pygame.QUIT:
                    done = True
                if pressed[self.master.K_ESCAPE]:
                    done = True
                self.master.display.flip()
        self.master.display.quit()
        self.master.quit()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    app = board(pygame)
    app.start_game()
