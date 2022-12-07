from utils import terminal, INF, actions, move, undo, score


def minimax(grid, computer, alpha, beta, depth):
    # Return the maximum value a player can obtain at each step
    if terminal(grid):
        return score(grid), depth

    if computer:
        func = max
        m = -INF
        char = 1
    else:
        func = min
        m = INF
        char = -1

    # For every possible action
    for action in actions(grid):
        row, col = action

        # Update grid
        move(grid, row, col, char)

        # Calculate maximum value for this action
        value, depth = minimax(grid, not computer, alpha, beta, depth + 1)

        m = func(m, value)

        # Undo the move
        undo(grid, row, col)

        # Alpha-beta pruning
        if computer:
            alpha = func(alpha, m)
        else:
            beta = func(beta, m)

        if beta <= alpha:
            break

    return m, depth


def minimax_best_move(grid):
    # Find all empty cells and compute the minimax for each one
    m = alpha = -INF
    d = beta = INF

    # For every possible action
    result = None
    for action in actions(grid):
        row, col = action
        move(grid, row, col, 1)
        value, depth = minimax(grid, False, alpha, beta, 0)
        if value > m or (value == m and depth < d):
            result = row, col
            m = value
            d = depth
        # undo the move
        undo(grid, row, col)
    return {'row': result[0], 'col': result[1]}
