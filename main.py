import keyboard
from game import *
import time

key_mapping = {
    'flecha abajo': Movement.DOWN,
    'down': Movement.DOWN,
    's': Movement.DOWN,
    'flecha derecha': Movement.RIGHT,
    'right': Movement.RIGHT,
    'd': Movement.RIGHT,
    'flecha izquierda': Movement.LEFT,
    'left': Movement.LEFT,
    'a': Movement.LEFT,
    'space': Movement.ROTATE
}


def main():
    '''## Summary
    The `main` function is the entry point of the program. It initializes the game board, prints the initial board, and then enters a loop to handle user input and update the game state until the game is over or the user presses the 'esc' key.

    ## Example Usage
    ```python
    main()
    ```
    ## Code Analysis
    ### Inputs
    - None
    ### Flow
    1. Initialize the game board.
    2. Print the initial board.
    3. Set the initial values for the `key` and `game_over` variables.
    4. Enter a loop that continues until the user presses the 'esc' key or the game is over.
    5. Read the user's keyboard input.
    6. If the input is a key press event, check if it is a valid key for moving the game piece.
    7. If it is a valid key, move the game piece accordingly on the game board.
    8. Check if the game is over by iterating through the first row of the game board and checking if any cell is not empty.
    9. If the game is over, set the `game_over` variable to True to exit the loop.
    ### Outputs
    - None
    '''
    # Initializing the game
    board = Board()

    # Printing the initial board
    board.print_board()

    key = None
    game_over = False
    # The Key 'escape' exit the game
    while (key != 'esc' and not game_over):
        listener = keyboard.read_event()

        if listener.event_type == keyboard.KEY_DOWN:
            key = listener.name
            if key in key_mapping:
                board.move_piece(key_mapping[key])

        for cell in board.boxes[0]:
            if cell != "⬜":
                game_over = True
                break

    print("Game Over")


if __name__ == '__main__':
    main()
