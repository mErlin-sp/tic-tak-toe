import numpy as np

from display import render
from settings import size

INF = np.inf  # infinity


def move(grid, row, col, player):
    """Update grid on new move"""
    grid[row][col] = player


def undo(grid, row, col):
    """Undo move on grid"""
    grid[row][col] = 0


def get_user_input(grid):
    while True:
        render(grid)
        print("   ENTER ROW AND COLUMN")
        choice = input("   > ").split()
        try:
            row, col = map(int, choice)
            # If Cell is out of bounds
            if row < 0 or row > size:
                continue
            elif col < 0 or col > size:
                continue
            elif grid[row][col] != 0:
                continue
            else:
                return row, col
        except:
            continue


def win_player(grid, char):
    # Check if a player wins the game

    # Check for rows, columns and diagonals
    result = char * size in grid.sum(axis=1)
    result = result or char * size in grid.sum(axis=0)
    result = result or char * size == np.trace(grid)
    result = result or char * size == np.trace(np.fliplr(grid))
    return result


def terminal(grid):
    # Check if the game is at a terminal state
    # A game is in terminal state if either player wins or it's a tie
    return win_player(grid, -1) or win_player(grid, 1) or 0 not in grid


def score(grid, depth=1, player=1):
    # Return the score corresponding to the terminal state
    if win_player(grid, -1):
        return (-1 / depth) * player
    if win_player(grid, 1):
        return (1 / depth) * player
    return 0


def actions(grid):
    # Return all possible actions a player can take at each state
    result = np.where(grid == 0)
    result = np.transpose(result)
    np.random.shuffle(result)
    return result
