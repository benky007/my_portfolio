import pygame
from pygame_noughts_and_crosses import *


class connect:
    def __init__(self, master):
        self.master = master
        self.screen = master.display.set_mode((500, 500))
        self.box_x = 0
        self.boxy = 0
        self.box = 0
        self.num_player = 0
        self.x = 0
        self.y = 0
        self.wins_count = 0
        self.wins1 = ["", 0, 0, 0, 0]
        self.wins2 = ["", 0, 0, 0, 0]
        self.wins = ["", 0, 0, 0, 0]
        self.end = 0
        self.start = 0
        self.now = 0
        self.starting = 0
        self.ai_name = ""
        self.player1_name = ""
        self.player2_name = ""
        self.start1 = 0
        self.name1_png = "O&XN1.png"
        self.name2_png = "O&XN2.png"
        self.win1_png = "O&X1w.png"
        self.win2_png = "O&X2w.png"
        self.player2_png = "O&X2P.png"
        self.ai_png = "O&XAI.png"
        self.draw_png = "O&Xd.png"
        self.lose_png = "O&XL.png"
        self.win_png = "O&XW.png"
        self.start_png = "O&XS.png"
        self.black_png = "black.png"
        self.pointsL = [(10, 410), (90, 410), (90, 490), (10, 490)]
        self.pointsR = [(410, 410), (490, 410), (490, 490), (410, 490)]
        self.buttons = [(70, 215), (320, 215)]
        self.screen.fill((0, 0, 0))
        self.font = self.master.font.SysFont('Arial', 20)
        self.file = "scores_connect.txt"
        self.start_connect()

    def start_connect(self):
        start = game(pygame)
        start.start_game()


if __name__ == '__main__':
    pygame.init()
    app = connect(pygame)
