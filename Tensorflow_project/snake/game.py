import pygame
import random


class Fruit:
    def __init__(self):
        self.current = 0

    def new(self, board):
        if self.current == 0:
            X, Y = random.randint(0, 22), random.randint(0, 22)
            board[Y][X] = 4
            self.current += 1
            cords = (X, Y)
            return cords
        else:
            pass


class Snake:
    def __init__(self):
        self.direction = random.choice(["u", "d", "l", "r"])
        self.body = []

    def left(self):
        self.direction = "l"
        X_change = -1
        Y_change = 0
        return self.direction, X_change, Y_change

    def right(self):
        self.direction = "r"
        X_change = 1
        Y_change = 0
        return self.direction, X_change, Y_change

    def up(self):
        self.direction = "u"
        X_change = 0
        Y_change = 1
        return self.direction, X_change, Y_change

    def down(self):
        self.direction = "d"
        X_change = 0
        Y_change = -1
        return self.direction, X_change, Y_change

    def calculate(self, board, snake, fruit, x_change, y_change):
        X1 = snake[0]
        Y1 = snake[1]
        if X1 + x_change == fruit[0] and Y1 - y_change == fruit[1] and self.direction != "":
            print("1")
            self.body.insert(0, (X1, Y1))
            board[Y1][X1] = 1
            eaten = True
        elif self.direction != "":
            self.body.insert(0, (X1, Y1))
            board[Y1][X1] = 1
            board[self.body[len(self.body)-1][1]][self.body[len(self.body)-1][0]] = 0
            self.body.pop(len(self.body)-1)
            eaten = False
        if snake[0] == 0 and x_change == -1:
            print("4")
            running = False
        elif snake[0] == 22 and x_change == 1:
            print("5")
            running = False
        elif snake[1] == 0 and y_change == 1:
            print("6")
            running = False
        elif snake[1] == 22 and y_change == -1:
            print("7")
            running = False
        elif board[Y1 - y_change][X1 + x_change] == 1:
            print("8")
            running = False
        else:
            print("9")
            X1 = X1 + x_change
            Y1 = Y1 - y_change
            board[Y1][X1] = 2
            running = True
            snake = (X1, Y1)
        return running, board, snake, eaten

    @staticmethod
    def current(board):
        count = 0
        for count1, i in enumerate(board):
            for count2, n in enumerate(i):
                if n == 2:
                    X = count2
                    Y = count1
                else:
                    count += 1
        if count == len(board) * len(board[0]):
            board[11][11] = 2
            board[22][22] = 0
            X = 11
            Y = 11
        else:
            X = X
            Y = Y
        return board, X, Y


class game:
    def __init__(self, master):
        self.master = master
        self.WIDTH = 500
        self.HEIGHT = 500
        self.FPS = 750

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)

        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.screen = self.master.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen.fill((0, 0, 0))
        self.font = self.master.font.SysFont('Arial', 20)
        self.master.display.set_caption("My Game")
        self.clock = self.master.time.Clock()
        self.count = 0
        count = 0
        self.ratio = self.setup(count)
        self.snake = Snake()
        self.fruit = Fruit()
        self.master.display.flip()
        self.game_loop()

    def setup(self, count):
        self.screen.fill((0, 0, 0))
        self.master.draw.rect(self.screen, self.WHITE, self.master.Rect(20, 20, 460, 460))
        self.master.draw.rect(self.screen, self.BLACK, self.master.Rect(21, 21, 458, 458))
        i = 0
        step = int(460 / len(self.board))
        while i < 460:
            self.master.draw.line(self.screen, self.WHITE, (i + step, step), (i + step, 479))
            self.master.draw.line(self.screen, self.WHITE, (step, i + step), (479, i + step))
            i += step
        if count == 0:
            count += 1
            return step

    def update(self, board):
        self.setup(1)
        for count1, i in enumerate(board):
            for count2, n in enumerate(i):
                if n == 1 or n == 2 or n == 3:
                    X = count2 + 1
                    Y = count1 + 1
                    if n == 1:
                        colour = self.RED
                    elif n == 2:
                        colour = self.GREEN
                    else:
                        colour = self.YELLOW
                    self.master.draw.rect(self.screen, colour,
                                          self.master.Rect(self.ratio * X + 1, self.ratio * Y + 1, self.ratio - 1,
                                                           self.ratio - 1))
                if n == 4:
                    X = count2 + 1
                    Y = count1 + 1
                    self.master.draw.rect(self.screen, self.BLUE,
                                          self.master.Rect(self.ratio * X + 1, self.ratio * Y + 1, self.ratio - 1,
                                                           self.ratio - 1))

    def game_loop(self):
        running = True
        eaten = True
        wait = False
        direction = self.snake.direction
        X_change = 0
        Y_change = 0
        board, hX, hY = self.snake.current(self.board)
        while running:
            self.clock.tick(self.FPS)
            if eaten:
                testing = True
                head = (hX, hY)
                count1 = 0
                fruit = (10, 11)
                while testing:
                    if count1 == 0:
                        self.fruit.current = 0
                        fruit = self.fruit.new(board)
                        count1 += 1
                    else:
                        fruit = fX, fY
                    count = 0
                    for i in self.snake.body:
                        if i == fruit or head == fruit:
                            self.fruit.current = 0
                            fX, fY = self.fruit.new(board)
                            testing = False
                        else:
                            count += 1
                    if count == len(self.snake.body):
                        testing = False
                (fX, fY) = fruit
                eaten = False
            for event in self.master.event.get():
                if event.type == self.master.QUIT:
                    self.master.display.quit()
                    self.master.quit()
            try:
                pressed = self.master.key.get_pressed()
            except pygame.error:
                pass
            if pressed[self.master.K_ESCAPE]:
                running = False
            if pressed[self.master.K_UP] and direction != "d" and not wait:
                direction = "u"
                wait = True
            if pressed[self.master.K_RIGHT] and direction != "l" and not wait:
                direction = "r"
                wait = True
            if pressed[self.master.K_LEFT] and direction != "r" and not wait:
                direction = "l"
                wait = True
            if pressed[self.master.K_DOWN] and direction != "u" and not wait:
                direction = "d"
                wait = True
            if direction == "u":
                direction, X_change, Y_change = self.snake.up()
            elif direction == "d":
                direction, X_change, Y_change = self.snake.down()
            elif direction == "l":
                direction, X_change, Y_change = self.snake.left()
            elif direction == "r":
                direction, X_change, Y_change = self.snake.right()
            if self.count % 100 == 1:
                running, board, (hX, hY), eaten = self.snake.calculate(board, (hX, hY), (fX, fY), X_change,
                                                                       Y_change)
                wait = False

            self.count += 1
            self.update(board)
            try:
                pygame.display.flip()
            except self.master.error:
                pass

        self.fail()

    def fail(self):
        waiting = True
        self.screen.fill((0, 0, 0))
        lost = self.font.render("You lost press enter to play again or escape to leave", True, (255, 0, 0))
        width, height = self.font.size("You lost press enter to play again or escape to leave")
        self.screen.blit(lost, (0, 0))
        while waiting:
            for event in self.master.event.get():
                if event.type == self.master.QUIT:
                    waiting = False
                    leave = True
            try:
                pressed = self.master.key.get_pressed()
            except pygame.error:
                pass
            if pressed[self.master.K_ESCAPE]:
                waiting = False
                leave = True
            if pressed[self.master.K_RETURN]:
                waiting = False
                leave = False

            try:
                self.master.display.flip()
            except self.master.error:
                pass

        if leave:
            self.master.display.quit()
            self.master.quit()
        else:
            self.screen.fill((0, 0, 0))
            self.__init__(self.master)


if __name__ == '__main__':
    pygame.init()
    app = game(pygame)
