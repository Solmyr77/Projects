import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player


tic_tac_toe = TicTacToe()
tic_tac_toe.create_board()
print (tic_tac_toe.board)
