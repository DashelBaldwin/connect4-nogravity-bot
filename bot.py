# bot.py 

import numpy as np

class Board:
    def __init__(self, width, height):
        # TODO enforce this via input validation
        assert width >= 4 and height >= 4

        self.width = width
        self.height = height
        self.contents = [[None] * width for _ in range(height)]


    def place(self, player, row, col):

        self.contents[row][col] = player


    def _check_seq(self, seq) -> bool:
        """Checks if 4 in a row exists within in a sequence."""
        # TODO change 0 to None

        for i in range(max(len(seq)-4, 1)): # max() ensures a segment will still be generated if len(sequence) is 4
            segment = seq[i:i+4]

            if len(set(segment)) == 1 and 0 not in segment:
                return True

        return False
    

    def _compress_cols(self) -> list:
        """Returns each column of the board."""
        return list(zip(*self.contents))
    

    def _compress_diags(self) -> list:
        """Returns each diagonal of the board."""
        down_right =  [tuple(np.diagonal(self.contents, i)) for i in range(4 - self.height, self.width - 3)]
        down_left = [tuple(np.fliplr(self.contents).diagonal(i)) for i in range(4 - self.height, self.width - 3)]

        return down_right + down_left


    def check_win(self) -> bool:
        """Checks if four in a row exists anywhere."""
        compressed = self._compress_diags()[:] + self._compress_cols()[:] + [tuple(i) for i in self.contents][:]

        for seq in compressed:
             if self._check_seq(seq):
                 return True
        return False


    def display(self):
        for row in self.contents:
            for player_ref in row:
                if player_ref:
                    print(player_ref.icon, end=" ")
                else:
                    print("░", end=" ")
            print()



class Player():
    def __init__(self, icon):
        self.icon = icon


p1 = Player("X")
p2 = Player("O")


    




def temp():
    board = Board(5, 5)
    for i in range(4):
        board.place(p2, 0, i)
    board.display()
    print(board.check_win())