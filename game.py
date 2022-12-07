import numpy as np

from display import render
from negascout import negascout
from settings import size
from utils import move, get_user_input, win_player, terminal, INF


def game_loop(grid):
    while True:
        # Player turn
        row, col = get_user_input(grid)
        move(grid, row, col, -1)
        render(grid)

        # Check if the player wins
        if win_player(grid, -1):
            print("   YOU WIN!")
            break
        # Check if it's a tie
        if terminal(grid):
            print("   TIE!")
            break

        # Computer turn
        # Use minimax algorithm
        # best_move = minimax_best_move(grid)

        # Use negamax algorithm
        # best_move = negamax(grid, 0, 1)

        # Use negamax algorithm with alpha-beta pruning
        # best_move = negamax_ab_pruning(grid, 0, -INF, INF, 1)

        # Use negascout algorithm
        best_move = negascout(grid, 0, -INF, INF, 1)

        row = best_move['row']
        col = best_move['col']

        move(grid, row, col, 1)
        render(grid)

        # Check if machine wins
        if win_player(grid, 1):
            print("   YOU LOSE!")
            break


def play():
    while True:
        # Initialize empty grid
        grid = np.zeros((size, size), int)
        game_loop(grid)

        print("   PLAY AGAIN ? [Y/N]")
        again = input("   > ")
        if again.upper() != "Y":
            break


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        print("\n   KEYBOARD INTERRUPT : ABORT")
