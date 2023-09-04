from enum import Enum
import os

class Movement(Enum):
    DOWN = 0
    RIGHT = 1
    LEFT = 2
    ROTATE = 3


class Game:
    '''
    The `Game` class represents a game board and provides methods to move and rotate a piece on the board.
    '''
    ROTATION_POSITIONS = [[(1,1),(0,0),(0,-2),(-1,-1)],
                          [(2,0),(1,-1),(0,0),(-1,1)],
                          [(1,1),(0,2),(0,0),(-1,-1)],
                          [(1,-1),(0,0),(-1,1),(-2,0)]]

    def __init__(self):
        self.board = [["🟦", "⬜"*9],
                      ["🟦", "🟦", "🟦", "⬜"*7]] + [["⬜"]*10 for _ in range(8)]

        self.rotation = 0

    def print_board(self) -> None:
        os.system('cls')
        for row in self.board:
            print("".join(row))

        print('\n')

    def move_piece(self, movement: Movement)->None:
        '''The `move_piece` function in Python takes a movement as input and updates the game board
        accordingly, including rotating the piece if specified.
        
        Parameters
        ----------
        movement : Movement
            The `movement` parameter is an instance of the `Movement` enum. It represents the type of
        movement that should be applied to the piece. The possible values of the `Movement` enum are:
        
        Returns
        -------
            In the `move_piece` method, if the conditions in the `if` statement are not met (i.e.,
        `new_row_ind` is greater than 9 or `new_column_ind` is less than 0 or greater than 9), the
        method will return without making any changes to the board.
        
        '''
        # Initializing an empty board
        new_board = [["⬜"]*10 for _ in range(10)]
        piece_position = 0

        if movement == Movement.ROTATE:
            self.rotation = 0 if self.rotation == 3 else self.rotation+1

        # Running the original dashboard
        for row_ind, row in enumerate(self.board):
            for column_ind, box in enumerate(row):
                if box == "🟦":

                    new_row_ind = 0
                    new_column_ind = 0

                    match movement:
                        case Movement.DOWN:
                            new_column_ind = column_ind
                            new_row_ind = row_ind + 1                            
                        case Movement.RIGHT:
                            new_column_ind = column_ind + 1
                            new_row_ind = row_ind                            
                        case Movement.LEFT:
                            new_column_ind = column_ind - 1
                            new_row_ind = row_ind                            
                        case Movement.ROTATE:
                            new_column_ind = column_ind + self.ROTATION_POSITIONS[self.rotation][piece_position][0]
                            new_row_ind = row_ind + self.ROTATION_POSITIONS[self.rotation][piece_position][1]
                            piece_position+=1

                    if new_row_ind <= 9 and (new_column_ind >= 0 and new_column_ind <= 9):
                        new_board[new_row_ind][new_column_ind] = "🟦"
                    else:
                        return

        self.board = new_board
        self.print_board()
