import keyboard
from game import Game, Movement

def main():
    # Initializing the game
    tetris = Game()
    # Printing the initial board
    tetris.print_board()

    key = None

    # The Key 'escape' exit the game
    while(key != 'esc'):
        listener = keyboard.read_event()

        if listener.event_type == keyboard.KEY_DOWN:
            key = listener.name
            if key == 'flecha abajo' or key =='s':
                tetris.move_piece(Movement.DOWN)

            elif key == 'flecha derecha' or key =='d':
                tetris.move_piece(Movement.RIGHT)

            elif key == 'flecha izquierda' or key =='a':
                tetris.move_piece(Movement.LEFT)

            elif key == 'space':
                tetris.move_piece(Movement.ROTATE)

if __name__ == '__main__':
    main()