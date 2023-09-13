import keyboard
from game import *


def main():
    # Initializing the game
    board = Board()

    # Printing the initial board
    board.print_board()

    key = None
    end = False
    # The Key 'escape' exit the game
    while (key != 'esc' and not end):
        listener = keyboard.read_event()

        if listener.event_type == keyboard.KEY_DOWN:
            key = listener.name
            if key == 'flecha abajo' or key == 's':
                board.move_piece(Movement.DOWN)

            elif key == 'flecha derecha' or key == 'd':
                board.move_piece(Movement.RIGHT)

            elif key == 'flecha izquierda' or key == 'a':
                board.move_piece(Movement.LEFT)

            elif key == 'space':
                board.move_piece(Movement.ROTATE)


if __name__ == '__main__':
    main()
