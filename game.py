from game import _JBlock, _IBlock, _LBlock, _SquareBlock, _TBlock, _ZBlock, _SBlock
from typing import Union
import random
import os
from enum import Enum
import copy


COLOURS = ('🟦', '🟥', '🟪', '🟩', '🟧', '🟨')


class Movement(Enum):
    ''' 
    MOVEMENT
    ---- 
    The class `Movement` is an enumeration that represents different types of movements.
    '''
    DOWN = 0
    RIGHT = 1
    LEFT = 2
    ROTATE = 3


class Board():
    ''' 
    BOARD
    ----
    The `Board` class represents a game board and manages the movement and placement of pieces on the
    board.'''

    BOARD = [["⬜"]*10 for _ in range(10)]

    def __init__(self):
        self.boxes = self.BOARD
        self.piece = Piece()

    def print_board(self) -> None:
        os.system('cls')
        print('\033[91m ESC to exit')
        # Hacer una copia temporal del tablero
        temp_board = copy.deepcopy(self.boxes)

        for position in self.piece.shape.position:
            temp_board[position[1]][position[0]] = self.piece.colour

        for row in temp_board:
            print("".join(map(str, row)))

        print('\n')

    def update_board(self):
        for position in self.piece.shape.position:
            self.boxes[position[1]][position[0]] = self.piece.colour

        self.piece.change_piece()

    def move_piece(self, movement: Movement) -> None:
        if movement == Movement.ROTATE:
            self.piece.rotation_state = 0 if self.piece.rotation_state == 3 else self.piece.rotation_state+1

        if self._is_valid_move(movement):
            for box_index, box in enumerate(self.piece.shape.position):
                match movement:
                    case Movement.DOWN:
                        box[1] += 1
                    case Movement.RIGHT:
                        box[0] += 1
                    case Movement.LEFT:
                        box[0] -= 1
                    case Movement.ROTATE:
                        box[0] += self.piece.shape.rotation[self.piece.rotation_state][box_index][0]
                        box[1] += self.piece.shape.rotation[self.piece.rotation_state][box_index][1]
                        self._rotation_control(box)

        self.print_board()

    def _is_valid_move(self, movement: Movement) -> bool:
        for box in self.piece.shape.position:
            match movement:
                case Movement.DOWN:
                    if box[1] >= 9:
                        self.update_board()
                        return False
                case Movement.RIGHT:
                    if box[0] >= 9:
                        return False
                case Movement.LEFT:
                    if box[0] <= 0:
                        return False
        return True

    def _rotation_control(self, box) -> None:
        if box[0] < 0:
            for item in self.piece.shape.position:
                item[0] += 1

        if box[0] > 9:
            for item in self.piece.shape.position:
                item[0] -= 1

        if box[1] > 9:
            for item in self.piece.shape.position:
                item[1] -= 1


class Piece:
    def __init__(self):
        self.colour = COLOURS[random.randint(0, len(COLOURS)-1)]
        self.shape = self._random_shape()
        self.rotation_state = 0

    def _random_shape(self) -> Union[_JBlock, _IBlock, _LBlock, _SquareBlock, _TBlock, _ZBlock, _SBlock]:
        '''The function randomly selects and returns an instance of a shape class from a list of available
        shapes.

        Returns
        -------
            an instance of a randomly selected shape class.

        '''
        # List of available shapes
        pieces = [_JBlock, _IBlock, _LBlock,
                  _SquareBlock, _TBlock, _ZBlock, _SBlock]

        # Selecting random shape class
        selected_piece = random.choice(pieces)

        # Returning and instantiating random shape
        return selected_piece()

    def change_piece(self):
        # Selecting random colour
        self.colour = COLOURS[random.randint(0, len(COLOURS)-1)]
        # Selecting random shape
        self.shape = self._random_shape()
        # Reseting rotation state
        self.rotation_state = 0


class _JBlock:
    '''🟦⬜⬜\n
        🟦🟦🟦\n
        ⬜⬜⬜'''

    def __init__(self):
        self.position = [[0, 0], [0, 1], [1, 1], [2, 1]]
        self.rotation = [[(0, -2), (-1, -1), (0, 0), (1, 1)],
                         [(2, 0), (1, -1), (0, 0), (-1, 1)],
                         [(0, 2), (1, 1), (0, 0), (-1, -1)],
                         [(-2, 0), (-1, 1), (0, 0), (1, -1)]]


class _IBlock:
    '''🟦🟦🟦🟦'''

    def __init__(self):
        self.position = [[0, 1], [1, 1], [2, 1], [3, 1]]
        self.rotation = [[(-1, -2), (0, -1), (1, 0), (2, 1)],
                         [(2, -1), (1, 0), (0, 1), (-1, 2)],
                         [(1, 2), (0, 1), (-1, 0), (-2, -1)],
                         [(-2, 1), (-1, 0), (0, -1), (1, -2)]]


class _LBlock:
    '''⬜⬜🟦 \n
    🟦🟦🟦\n
    ⬜⬜⬜'''

    def __init__(self):
        self.position = [[2, 0], [2, 1], [1, 1], [0, 1]]
        self.rotation = [[(2, 0), (1, 1), (0, 0), (-1, -1)],
                         [(0, 2), (-1, 1), (0, 0), (1, -1)],
                         [(-2, 0), (-1, -1), (0, 0), (1, 1)],
                         [(0, -2), (1, -1), (0, 0), (-1, 1)]]


class _SquareBlock:
    '''🟦🟦\n
    🟦🟦'''

    def __init__(self):
        self.position = [[1, 0], [2, 0], [1, 1], [2, 1]]
        self.rotation = [[(0, 0), (0, 0), (0, 0), (0, 0)],
                         [(0, 0), (0, 0), (0, 0), (0, 0)],
                         [(0, 0), (0, 0), (0, 0), (0, 0)],
                         [(0, 0), (0, 0), (0, 0), (0, 0)]]


class _TBlock:
    '''🟦🟦🟦\n
    ⬜🟦⬜'''

    def __init__(self):
        self.position = [[1, 0], [0, 1], [1, 1], [2, 1]]
        self.rotation = [[(1, -1), (-1, -1), (0, 0), (1, 1)],
                         [(1, 1), (1, -1), (0, 0), (-1, 1)],
                         [(-1, 1), (1, 1), (0, 0), (-1, -1)],
                         [(-1, -1), (-1, 1), (0, 0), (1, -1)]]


class _ZBlock:
    def __init__(self):
        self.position = [[0, 0], [1, 0], [1, 1], [2, 1]]
        self.rotation = [[(0, -2), (1, -1), (0, 0), (1, 1)],
                         [(2, 0), (1, 1), (0, 0), (-1, 1)],
                         [(0, 2), (-1, 1), (0, 0), (-1, -1)],
                         [(-2, 0), (-1, -1), (0, 0), (1, -1)]]


class _SBlock:
    def __init__(self):
        self.position = [[2, 0], [1, 0], [1, 1], [0, 1]]
        self.rotation = [[(2, 0), (1, -1), (0, 0), (-1, -1)],
                         [(0, 2), (1, 1), (0, 0), (1, -1)],
                         [(-2, 0), (-1, 1), (0, 0), (1, 1)],
                         [(0, -2), (-1, -1), (0, 0), (-1, 1)]]
