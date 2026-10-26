import pygame
import time
import random
import json


class AI_OX:
    def __init__(self, game_board, end, turn):
        self.game_board = game_board
        self.count = 0
        self.count1 = 0
        self.dict1 = {}
        self.end = end
        self.place = 0
        self.player = (0, 0)
        self.turn = turn

    def choose(self):
        if self.end == 0:
            ai = True
            while ai:
                place = random.randint(0, 8)
                if self.game_board[place] == 0:
                    self.game_board[place] = 1
                    self.player = (1, place)
                    self.turn = (self.turn + 1) % 2
                    ai = False
                else:
                    pass
        if self.end == 1:
            pass
        result = (self.game_board, self.player, self.turn)
        return result


class game:
    def __init__(self, master):
        self.master = master
        self.screen = master.display.set_mode((500, 500))
        self.box_x = 0
        self.boxy = 0
        self.box = 0
        self.num_player = 0
        self.x = 0
        self.y = 0
        self.dict1 = {}
        self.wins_count = 0
        self.count = 0
        self.count1 = 0
        self.wins1 = ["", 0, 0, 0, 0]
        self.wins2 = ["", 0, 0, 0, 0]
        self.wins = ["", 0, 0, 0, 0]
        self.end = 0
        self.turn = 0
        self.nought = 0
        self.start = 0
        self.now = 0
        self.starting = 0
        self.ai_name = ""
        self.player1_name = ""
        self.player2_name = ""
        self.start1 = 0
        self.current = 0
        self.win_check = ["", 0, 0, 0, 0]
        self.win_check1 = ["", 0, 0, 0, 0]
        self.win_check2 = ["", 0, 0, 0, 0]
        self.checking = []
        self.checking1 = []
        self.checking2 = []
        self.pointsL = [(10, 410), (90, 410), (90, 490), (10, 490)]
        self.pointsR = [(410, 410), (490, 410), (490, 490), (410, 490)]
        self.list1 = [(100, 100), (200, 100), (300, 100),
                      (100, 200), (200, 200), (300, 200),
                      (100, 300), (200, 300), (300, 300)]
        self.buttons = [(70, 215), (320, 215)]
        self.game_board = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0]
        self.screen.fill((0, 0, 0))
        self.font = self.master.font.SysFont('Arial', 20)
        self.file = "scores.json"
        self.start_game()

    def name1(self):
        font = self.master.font.SysFont('Arial', 150)
        image = pygame.image.load("O&XN1.png")
        self.end = 0
        text = ["", "", ""]
        input_active = True
        current = 0
        run = True
        while run:
            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if event.type == self.master.QUIT:
                    run = False
                    self.master.display.quit()
                    self.master.quit()
                if pressed[self.master.K_ESCAPE]:
                    run = False
                    self.master.display.quit()
                    self.master.quit()
                elif event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_RETURN:
                        self.ai_name = text[0] + text[1] + text[2]
                        input_active = False
                        run = False
                    elif event.key == pygame.K_BACKSPACE:
                        text[current] = ""
                    else:
                        text[current] = event.unicode.upper()
                        current += 1
                        if current > 2:
                            current = 2

                try:
                    self.screen.blit(image, (0, 0))
                except pygame.error:
                    pass
                try:
                    text_surf1 = font.render(text[0], True, (255, 0, 0))
                    text_surf2 = font.render(text[1], True, (255, 0, 0))
                    text_surf3 = font.render(text[2], True, (255, 0, 0))
                except pygame.error:
                    pass
                if current == 0:
                    pygame.draw.rect(self.screen, (255, 0, 0), (110, 350, 80, 25))
                if current == 1:
                    pygame.draw.rect(self.screen, (255, 0, 0), (210, 350, 80, 25))
                if current == 2:
                    pygame.draw.rect(self.screen, (255, 0, 0), (310, 350, 80, 25))
                (text1x, text1y) = font.size(text[0])
                self.screen.blit(text_surf1, (110 + ((80 - text1x) / 2), 375 - text1y))
                (text2x, text2y) = font.size(text[1])
                self.screen.blit(text_surf2, (210 + ((80 - text2x) / 2), 375 - text2y))
                (text3x, text3y) = font.size(text[2])
                self.screen.blit(text_surf3, (310 + ((80 - text3x) / 2), 375 - text3y))
                try:
                    self.master.display.flip()
                except pygame.error:
                    pass
            time.sleep(.2)
        pygame.draw.rect(self.screen, (255, 0, 0), (110, 350, 80, 25))
        pygame.draw.rect(self.screen, (255, 0, 0), (210, 350, 80, 25))
        pygame.draw.rect(self.screen, (255, 0, 0), (310, 350, 80, 25))
        pygame.display.flip()
        self.num_player = 1
        self.name_check()
        self.playerAI()

    def name2(self):
        try:
            font = self.master.font.SysFont('Arial', 100)
        except pygame.error:
            pass
        image = pygame.image.load("O&XN1.png")
        self.end = 0
        text = ["", "", ""]
        text1 = ["", "", ""]
        end = 0
        input_active = True
        current = 0
        player = 0
        run = True
        while run:
            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if event.type == self.master.QUIT:
                    run = False
                    self.master.display.quit()
                    self.master.quit()
                if pressed[self.master.K_ESCAPE]:
                    run = False
                    self.master.display.quit()
                    self.master.quit()
                elif event.type == pygame.KEYDOWN and input_active and player == 0:
                    if event.key == pygame.K_RETURN and text[0] != "" and text[1] != "" and text[2] != "":
                        self.player1_name = text[0] + text[1] + text[2]
                        player = 1
                        end = 1
                        current = 0
                    elif event.key == pygame.K_BACKSPACE:
                        text[current] = ""
                        current -= 1
                        if current < 0:
                            current = 0
                    else:
                        text[current] = event.unicode.upper()
                        current += 1
                        if current > 2:
                            current = 2

                elif event.type == pygame.KEYDOWN and input_active and player == 1:
                    if event.key == pygame.K_RETURN and text1[0] != "" and text1[1] != "" and text1[2] != "":
                        self.player2_name = text1[0] + text1[1] + text1[2]
                        input_active = False
                        run = False
                    elif event.key == pygame.K_BACKSPACE:
                        text1[current] = ""
                        current -= 1
                        if current < 0:
                            current = 0
                    else:
                        text1[current] = event.unicode.upper()
                        current += 1
                        if current > 2:
                            current = 2

                try:
                    self.screen.blit(image, (0, 0))
                except pygame.error:
                    pass
                try:
                    text_surf1 = font.render(text[0], True, (255, 0, 0))
                    text_surf2 = font.render(text[1], True, (255, 0, 0))
                    text_surf3 = font.render(text[2], True, (255, 0, 0))
                except pygame.error:
                    pass
                if end == 0:
                    if current == 0:
                        pygame.draw.rect(self.screen, (255, 0, 0), (15, 350, 60, 25))
                    if current == 1:
                        pygame.draw.rect(self.screen, (255, 0, 0), (95, 350, 60, 25))
                    if current == 2:
                        pygame.draw.rect(self.screen, (255, 0, 0), (175, 350, 60, 25))
                if end == 1:
                    pygame.draw.rect(self.screen, (255, 0, 0), (15, 350, 60, 25))
                    pygame.draw.rect(self.screen, (255, 0, 0), (95, 350, 60, 25))
                    pygame.draw.rect(self.screen, (255, 0, 0), (175, 350, 60, 25))
                (text1x, text1y) = font.size(text[0])
                self.screen.blit(text_surf1, (15 + ((60 - text1x) / 2), 366 - text1y))
                (text2x, text2y) = font.size(text[1])
                self.screen.blit(text_surf2, (95 + ((60 - text2x) / 2), 366 - text2y))
                (text3x, text3y) = font.size(text[2])
                self.screen.blit(text_surf3, (175 + ((60 - text3x) / 2), 366 - text3y))
                if player == 1:
                    try:
                        text_surf1 = font.render(text1[0], True, (255, 0, 0))
                        text_surf2 = font.render(text1[1], True, (255, 0, 0))
                        text_surf3 = font.render(text1[2], True, (255, 0, 0))
                    except pygame.error:
                        pass
                    if current == 0:
                        pygame.draw.rect(self.screen, (255, 0, 0), (265, 350, 60, 25))
                    if current == 1:
                        pygame.draw.rect(self.screen, (255, 0, 0), (345, 350, 60, 25))
                    if current == 2:
                        pygame.draw.rect(self.screen, (255, 0, 0), (425, 350, 60, 25))
                    (text1x, text1y) = font.size(text[0])
                    self.screen.blit(text_surf1, (265 + ((60 - text1x) / 2), 366 - text1y))
                    (text2x, text2y) = font.size(text[1])
                    self.screen.blit(text_surf2, (345 + ((60 - text2x) / 2), 366 - text2y))
                    (text3x, text3y) = font.size(text[2])
                    self.screen.blit(text_surf3, (425 + ((60 - text3x) / 2), 366 - text3y))
                try:
                    self.master.display.flip()
                except pygame.error:
                    pass
            time.sleep(.2)
        pygame.draw.rect(self.screen, (255, 0, 0), (265, 350, 60, 25))
        pygame.draw.rect(self.screen, (255, 0, 0), (345, 350, 60, 25))
        pygame.draw.rect(self.screen, (255, 0, 0), (425, 350, 60, 25))
        pygame.display.flip()
        self.num_player = 2
        self.name_check()
        self.player2()

    def name_check(self):
        count = 0
        count1 = 0
        count2 = 0
        if self.num_player == 1:
            with open("scores.json", "r") as file:
                data = json.load(file)
                scores = data["scores"]
                for o in range(len(data["scores"])):
                    if data["scores"][o]["name"] == self.ai_name and self.starting == 0:
                        self.wins = [scores[o]["name"], scores[o]["wins"], scores[o]["losses"],
                                     scores[o]["draws"], scores[o]["count"]]
                    else:
                        count += 1
                if count == len(data["scores"]):
                    self.wins = [self.ai_name, 0, 0, 0, 0]
                    with open(self.file, "r+") as f:
                        data1 = json.load(f)
                        data1["scores"].append({"name": self.wins[0], "wins": self.wins[1], "losses": self.wins[2],
                                                "draws": self.wins[3], "count": self.wins[4]})
                        f.seek(0)
                        json.dump(data1, f, indent=1)
            self.starting = 0
        if self.num_player == 2:
            with open(self.file, "r") as file:
                data = json.load(file)
                scores = data["scores"]
                for o in range(len(data["scores"])):
                    if data["scores"][o]["name"] == self.player1_name and self.starting == 0:
                        self.wins1 = [scores[o]["name"], scores[o]["wins"], scores[o]["losses"],
                                      scores[o]["draws"], scores[o]["count"]]
                    else:
                        count1 += 1
                    if data["scores"][o]["name"] == self.player2_name and self.starting == 0:
                        self.wins2 = [scores[o]["name"], scores[o]["wins"], scores[o]["losses"],
                                      scores[o]["draws"], scores[o]["count"]]
                    else:
                        count2 += 1
                if count1 == len(data["scores"]):
                    self.wins1 = [self.player1_name, 0, 0, 0, 0]
                    with open(self.file, "r+") as f:
                        data1 = json.load(f)
                        data1["scores"].append({"name": self.wins1[0], "wins": self.wins1[1],
                                                "losses": self.wins1[2], "draws": self.wins1[3],
                                                "count": self.wins1[4]})
                        f.seek(0)
                        json.dump(data1, f, indent=1)
                if count2 == len(data["scores"]):
                    self.wins2 = [self.player2_name, 0, 0, 0, 0]
                    with open(self.file, "r+") as f:
                        data1 = json.load(f)
                        data1["scores"].append({"name": self.wins2[0], "wins": self.wins2[1], "losses": self.wins2[2],
                                                "draws": self.wins2[3], "count": self.wins2[4]})
                        f.seek(0)
                        json.dump(data1, f, indent=1)
            self.starting = 0

    def start_game(self):
        image = pygame.image.load("O&XS.png")
        done = False
        self.end = 0
        while not done:
            for event in self.master.event.get():
                try:
                    pressed = self.master.key.get_pressed()
                except pygame.error:
                    pass
                if event.type == self.master.MOUSEBUTTONDOWN:
                    self.x, self.y = self.master.mouse.get_pos()
                    if event.button == 1:
                        for i in range(len(self.buttons)):
                            (self.box_x, self.boxy) = self.buttons[i]
                            for u in range(110):
                                if self.box_x + u == self.x:
                                    for p in range(100):
                                        if self.boxy + p == self.y:
                                            if i == 0:
                                                if self.player1_name == "" and self.player2_name == "":
                                                    self.name2()
                                                else:
                                                    self.player2()
                                            if i == 1:
                                                if self.ai_name == "":
                                                    self.name1()
                                                else:
                                                    self.playerAI()
                                            done = True
                if event.type == self.master.QUIT:
                    done = True
                    self.master.display.quit()
                    self.master.quit()
                if pressed[self.master.K_ESCAPE]:
                    done = True
                    self.master.display.quit()
                    self.master.quit()
                try:
                    self.screen.blit(image, (0, 0))
                    self.master.display.flip()
                except pygame.error:
                    pass
            time.sleep(.2)

    def player2(self):
        image = pygame.image.load("O&X2P.png")
        score1 = self.player1_name + " Score: " + str(self.wins1[1])
        score2 = self.player2_name + " Score: " + str(self.wins2[1])
        try:
            wins1 = self.font.render(score1, True, (0, 0, 0))
            wins2 = self.font.render(score2, True, (0, 0, 0))
            (width1, height1) = self.font.size(score1)
            (width2, height2) = self.font.size(score2)
            self.screen.blit(image, (0, 0))
        except pygame.error:
            pass
        self.master.draw.rect(self.screen, (255, 0, 0), pygame.Rect(0, 380, 100, 20))
        self.master.draw.rect(self.screen, (255, 0, 0), pygame.Rect(400, 380, 100, 20))
        self.screen.blit(wins1, (0 + ((100 - width1) / 2), 380 - ((height1 - 20) / 2)))
        self.screen.blit(wins2, (400 + ((100 - width2) / 2), 380 - ((height2 - 20) / 2)))
        self.master.draw.line(self.screen, (255, 0, 0), (200, 100), (200, 400), width=20)
        self.master.draw.line(self.screen, (255, 0, 0), (300, 100), (300, 400), width=20)
        self.master.draw.line(self.screen, (255, 0, 0), (100, 200), (400, 200), width=20)
        self.master.draw.line(self.screen, (255, 0, 0), (100, 300), (400, 300), width=20)
        self.num_player = 2
        self.wins1[4] = int(self.wins1[4]) + 1
        self.wins2[4] = int(self.wins2[4]) + 1
        if self.start == 0:
            self.check()

    def playerAI(self):
        image = pygame.image.load("O&XAI.png")
        score = self.ai_name + " Score: " + str(self.wins[1])
        try:
            wins = self.font.render(score, True, (0, 0, 0))
            (width, height) = self.font.size(score)
            self.screen.blit(image, (0, 0))
        except pygame.error:
            pass
        self.master.draw.line(self.screen, (255, 0, 0), (200, 100), (200, 400), width=20)
        self.master.draw.line(self.screen, (255, 0, 0), (300, 100), (300, 400), width=20)
        self.master.draw.line(self.screen, (255, 0, 0), (100, 200), (400, 200), width=20)
        self.master.draw.line(self.screen, (255, 0, 0), (100, 300), (400, 300), width=20)
        self.master.draw.rect(self.screen, (255, 0, 0), pygame.Rect(200, 440, 100, 20))
        self.screen.blit(wins, (200 + ((100 - width) / 2), 440 - ((height - 20) / 2)))
        self.num_player = 1
        self.wins[4] += 1
        if self.start == 0:
            self.check()

    def game_win(self, type):
        player = type
        if self.num_player == 2:
            if self.nought == 0 and self.turn == type:
                player = 1
            if self.nought == 1 and self.turn == type:
                player = 2
            if player > 2:
                player = 1
            if player == 1:
                image = pygame.image.load("O&X2w.png")
                self.wins2[1] = int(self.wins2[1]) + 1
                self.wins1[2] = int(self.wins1[2]) + 1
            if player == 2:
                image = pygame.image.load("O&X1w.png")
                self.wins1[1] = int(self.wins1[1]) + 1
                self.wins2[2] = int(self.wins2[2]) + 1
            try:
                self.screen.blit(image, (0, 0))
            except pygame.error:
                pass
            self.end = 1
            self.game_board = [0, 0, 0,
                               0, 0, 0,
                               0, 0, 0]
            self.start = 0
        if self.num_player == 1:
            if self.nought == 0 and self.turn == type:
                player = 1
            if self.nought == 1 and self.turn == type:
                player = 2
            if player > 2:
                player = 1
            if player == 1:
                image = pygame.image.load("O&XL.png")
                self.wins[2] = int(self.wins[2]) + 1
            if player == 2:
                image = pygame.image.load("O&XW.png")
                self.wins[1] = int(self.wins[1]) + 1
            try:
                self.screen.blit(image, (0, 0))
            except pygame.error:
                pass
            self.end = 1
            self.game_board = [0, 0, 0,
                               0, 0, 0,
                               0, 0, 0]
            self.start = 0

    def game_draw(self):
        self.count += 1
        image = pygame.image.load("O&Xd.png")
        if self.num_player == 1 and self.count == 1:
            self.wins[3] = int(self.wins[3]) + 1
        if self.num_player == 2 and self.count == 1:
            self.wins1[3] = int(self.wins1[3]) + 1
            self.wins2[3] = int(self.wins2[3]) + 1
        self.screen.blit(image, (0, 0))
        self.end = 1

    def wins_check(self, win_check, win_check1, win_check2):
        write = 0
        with open(self.file, "r") as f:
            data = json.load(f)
            ans = ""
            for scores in data["scores"]:
                if scores["name"] == win_check[0] and \
                        [scores["name"], scores["wins"], scores["losses"], scores["draws"], scores["count"]]\
                        != win_check and self.num_player == 1:
                    ans = {"name": self.ai_name, "wins": int(win_check[1]), "losses": int(win_check[2]),
                           "draws": int(win_check[3]), "count": int(win_check[4])}
                    write = 1
                if scores["name"] == win_check1[0] and \
                        [scores["name"], scores["wins"], scores["losses"], scores["draws"], scores["count"]] \
                        != win_check1 and self.num_player == 2:
                    ans = {"name": self.player1_name, "wins": int(win_check1[1]), "losses": int(win_check1[2]),
                           "draws": int(win_check1[3]), "count": int(win_check1[4])}
                    write = 1
                if scores["name"] == win_check2[0] and \
                        [scores["name"], scores["wins"], scores["losses"], scores["draws"], scores["count"]] \
                        != win_check2 and self.num_player == 2:
                    ans = {"name": self.player2_name, "wins": int(win_check2[1]), "losses": int(win_check2[2]),
                           "draws": int(win_check2[3]), "count": int(win_check2[4])}
                    write = 1
                if scores["name"] == win_check[0] and \
                        [scores["name"], scores["wins"], scores["losses"], scores["draws"], scores["count"]] \
                        == win_check and self.num_player == 1:
                    write = 0
                if scores["name"] == win_check1[0] and \
                        [scores["name"], scores["wins"], scores["losses"], scores["draws"], scores["count"]] \
                        == win_check1 and self.num_player == 2:
                    write = 0
                if scores["name"] == win_check2[0] and \
                        [scores["name"], scores["wins"], scores["losses"], scores["draws"], scores["count"]] \
                        == win_check2 and self.num_player == 2:
                    write = 0
                with open(self.file, "r+") as file:
                    if write == 1:
                        for i in range(len(data["scores"])):
                            if data["scores"][i] == scores:
                                data["scores"][i] = ans
                        file.seek(0)
                        json.dump(data, file, indent=1)
                        write = 0

    def game_check(self):
        for i in range(3):
            l = 0
            if i > 0:
                l = i * 3
            for e in range(2):
                if self.game_board[l] == e + 1 and self.game_board[l + 1] == e + 1 and self.game_board[l + 2] == e + 1:
                    self.game_win(e + 1)
                if self.game_board[i] == e + 1 and self.game_board[i + 3] == e + 1 and self.game_board[i + 6] == e + 1:
                    self.game_win(e + 1)
                if self.game_board[0] == e + 1 and self.game_board[4] == e + 1 and self.game_board[8] == e + 1:
                    self.game_win(e + 1)
                if self.game_board[2] == e + 1 and self.game_board[4] == e + 1 and self.game_board[6] == e + 1:
                    self.game_win(e + 1)
                if self.game_board[0] > 0 and self.game_board[1] > 0 and self.game_board[2] > 0 and \
                        self.game_board[3] > 0 and self.game_board[4] > 0 and self.game_board[5] > 0 and \
                        self.game_board[6] > 0 and self.game_board[7] > 0 and self.game_board[8] > 0:
                    self.game_draw()

    def draw(self, player):
        if player[0] == 1:
            cord_x, cordy = self.list1[player[1]]
            centre = (cord_x + 50, cordy + 50)
            self.master.draw.circle(self.screen, (255, 0, 0), centre, 30, 10)
        if player[0] == 2:
            cord_x, cordy = self.list1[player[1]]
            self.master.draw.line(self.screen, (255, 0, 0), (cord_x + 20, cordy + 20), (cord_x + 80, cordy + 80),
                                  width=10)
            self.master.draw.line(self.screen, (255, 0, 0), (cord_x + 80, cordy + 20), (cord_x + 20, cordy + 80),
                                  width=10)
        self.master.display.flip()
        time.sleep(0.5)

    def check(self):
        done = False
        while not done:
            for event in self.master.event.get():
                try:
                    pressed = self.master.key.get_pressed()
                except pygame.error:
                    pass
                if event.type == self.master.MOUSEBUTTONDOWN:
                    self.x, self.y = self.master.mouse.get_pos()
                    if event.button == 1:
                        for i in range(len(self.list1)):
                            (self.box_x, self.boxy) = self.list1[i]
                            for u in range(100):
                                if self.box_x + u == self.x:
                                    for p in range(100):
                                        if self.boxy + p == self.y:
                                            if self.game_board[i] == 0:
                                                if self.turn == 0:
                                                    self.game_board[i] = 2
                                                    player = (self.game_board[i], i)
                                                if self.turn == 1:
                                                    self.game_board[i] = 1
                                                    player = (self.game_board[i], i)
                                                self.turn = (self.turn + 1) % 2
                                                self.box = i
                                                self.draw(player)
                                                self.now = 1
                                                event.button = 2
                if self.end == 0:
                    self.game_check()
                if event.type == self.master.QUIT:
                    done = True
                    self.master.display.quit()
                    self.master.quit()
                if pressed[self.master.K_ESCAPE]:
                    done = True
                    self.master.display.quit()
                    self.master.quit()
                if pressed[self.master.K_RETURN]:
                    done = True
                image1 = pygame.image.load("black.png")
                if self.end == 0:
                    try:
                        self.screen.blit(image1, (0, 400))
                        self.screen.blit(image1, (400, 400))
                    except pygame.error:
                        pass
                    self.master.draw.line(self.screen, (255, 0, 0), (20, 420), (80, 470),
                                          width=10)
                    self.master.draw.line(self.screen, (255, 0, 0), (80, 420), (20, 470),
                                          width=10)
                    centre = (450, 450)
                    self.master.draw.circle(self.screen, (255, 0, 0), centre, 30, 10)
                    if self.turn == 0:
                        self.master.draw.lines(self.screen, (212, 175, 55), True, self.pointsL, 2)
                    if self.turn == 1:
                        self.master.draw.lines(self.screen, (212, 175, 55), True, self.pointsR, 2)
                        self.master.display.flip()
                        if self.num_player == 1:
                            AI = AI_OX(self.game_board, self.end, self.turn)
                            self.game_board, player, self.turn = AI.choose()
                            self.draw(player)
                if self.end == 0:
                    self.game_check()
                try:
                    self.master.display.flip()
                except pygame.error:
                    pass
            time.sleep(.2)
        AI_OX(self.game_board, self.end, self.turn)
        self.game_board = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0]
        self.end = 0
        self.now = 0
        self.count = 0
        self.count1 = 0
        self.wins_check(self.wins, self.wins1, self.wins2)
        try:
            self.start_game()
        except pygame.error:
            pass


if __name__ == '__main__':
    pygame.init()
    app = game(pygame)
