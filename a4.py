# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """
    def __init__(self):
        self.board = ['*' for _ in range(9)]
    
    def __str__(self) -> str:
        rows = []
        for i in range(3):
            row = ' '.join(self.board[i*3:(i + 1) * 3])
            rows.append(row)
        return '\n'.join(rows)
        
    def make_move(self, player, pos):
        """ Places a move for `player` in the position `pos` (where the board squares are 
        numbered from left to right, starting in the top left square with 0, and beginning
        at the left in each new row), if possible. '`player`' is a string ("X" or "O") 
        and `pos` is an integer. Returns `True` if the move was made and `False` if not
        (because the spot was full, or outside the boundaries of the board)."""
        if pos < 0 or pos >= 9:
            return False
        
        if self.board[pos] != '*':
            return False
        
        self.board[pos] = player
        return True
       
    def has_won(self, player): 
        """Returns `True` if `player` has won the game, and `False` if not """
        if (self.board[0] and self.board[1] and self.board[2] == player):
            return True
        elif (self.board[3] and self.board[4] and self.board[5] == player):
            return True
        elif (self.board[6] and self.board[7] and self.board[8] == player):
            return True
        elif (self.board[0] and self.board[4] and self.board[8] == player):
            return True
        elif (self.board[2] and self.board[4] and self.board[6] == player):
            return True
        elif (self.board[0] and self.board[3] and self.board[6] == player):
            return True
        elif (self.board[1] and self.board[4] and self.board[7] == player):
            return True
        elif (self.board[2] and self.board[5] and self.board[8] == player):
            return True
        return False
    def game_over(self): 
        """Returns `True` if someone has won or if the board is full, `False` otherwise"""
        if '*' not in self.board:
            return True
        if self.has_won() == True:
            return self.has_won()
        return False
    def clear(self): 
        """Clears the board to reset the game"""
        self.board = ['*' in range(9)]


def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    # uncomment to play!
    # play_tic_tac_toe()
