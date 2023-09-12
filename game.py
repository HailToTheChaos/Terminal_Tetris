import random
import os
from enum import Enum
import copy

COLOURS = ('🟦', '🟥', '🟪', '🟩')


class Movement(Enum):
    DOWN = 0
    RIGHT = 1
    LEFT = 2
    ROTATE = 3


class Board():
    BOARD = [["⬜"]*10 for _ in range(10)]

    def __init__(self):
        self.boxes = self.BOARD
        self.piece = Piece()

    def print_board(self) -> None:
        # Esto es para borrar la pantalla en Windows, puedes ajustarlo para tu sistema operativo.
        os.system('cls')

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

        if self._movement_control(movement):
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

        self.print_board()

    def _movement_control(self, movement: Movement) -> bool:
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


class Piece:
    def __init__(self):
        self.colour = COLOURS[random.randint(0, len(COLOURS)-1)]
        self.shape = self._random_shape()
        self.rotation_state = 0

    def _random_shape(self):
        # Lista de clases de piezas disponibles
        pieces = [_JBlock, _IBlock, _LBlock]

        # Selecciona una clase de pieza aleatoria
        selected_piece = random.choice(pieces)

        return selected_piece()

    def change_piece(self):
        self.colour = COLOURS[random.randint(0, len(COLOURS)-1)]
        self.shape = self._random_shape()
        self.rotation_state = 0


class _JBlock:
    def __init__(self):
        self.position = [[0, 0], [0, 1], [1, 1], [2, 1]]
        self.rotation = [[(0, -2), (-1, -1), (0, 0), (1, 1)],
                         [(2, 0), (1, -1), (0, 0), (-1, 1)],
                         [(0, 2), (1, 1), (0, 0), (-1, -1)],
                         [(-2, 0), (-1, 1), (0, 0), (1, -1)]]


class _IBlock:
    def __init__(self):
        self.position = [[0, 1], [1, 1], [2, 1], [3, 1]]
        self.rotation = [[(-1, -2), (0, -1), (1, 0), (2, 1)],
                         [(2, -1), (1, 0), (0, 1), (-1, 2)],
                         [(1, 2), (0, 1), (-1, 0), (-2, -1)],
                         [(-2, 1), (-1, 0), (0, -1), (1, -2)]]


class _LBlock:
    def __init__(self):
        self.position = [[2, 0], [2, 1], [1, 1], [0, 1]]
        self.rotation = [[[2, 0], [1, 1], (0, 0), (-1, -1)],
                         [(0, 2), (-1, 1), (0, 0), (1, -1)],
                         [(-2, 0), (-1, -1), (0, 0), (1, 1)],
                         [(0, -2), (1, -1), (0, 0), (-1, 1)]]
