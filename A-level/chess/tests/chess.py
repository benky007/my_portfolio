import tkinter


class game_board:
    def __init__(self, master):
        self.master = master


class piece:
    def __init__(self, piece_type, colour, player, pos):
        self.piece = piece_type
        self.colour = colour
        self.player = player
        self.name = self.colour + self.piece
        self.pos = pos

    def move(self, pos, board):
        all = self.possible_moves()
        piece = board[self.pos[1]][self.pos[0]]
        for possible in all:
            if pos == possible:
                board[pos[1]][pos[0]] = piece
                board[self.pos[1]][self.pos[0]] = ""


    def possible_moves(self):

    def taken(self):

    def take(self):


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("500x500")
    app = game_board(root)
    root.mainloop()

