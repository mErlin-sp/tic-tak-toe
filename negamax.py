from utils import terminal, actions, move, undo, score


def negamax(grid, depth, color):
    # Return the maximum value a player can obtain at each step
    if terminal(grid):
        return {'value': score(grid, depth, color)}

    results = []

    # For every possible action
    for action in actions(grid):
        row, col = action

        # Update grid
        move(grid, row, col, color)

        # Calculate maximum value for this action
        nm = negamax(grid, depth + 1, -color)
        nm['value'] = -nm['value']
        nm['row'] = row
        nm['col'] = col

        results.append(nm)

        # Undo the move
        undo(grid, row, col)

    return max(results, key=lambda vd: vd['value'])


def negamax_ab_pruning(grid, depth, alpha, beta, color):
    # Return the maximum value a player can obtain at each step
    if terminal(grid):
        return {'value': score(grid, depth, color)}

    value = None
    for action in actions(grid):
        row, col = action
        # Update grid
        move(grid, row, col, color)

        # Calculate maximum value for this action
        nm = negamax_ab_pruning(grid, depth + 1, -beta, -alpha, -color)
        nm['value'] = -nm['value']
        nm['row'] = row
        nm['col'] = col

        # Undo the move
        undo(grid, row, col)

        # Update the value
        value = nm if value is None else max(value, nm, key=lambda d: d['value'])

        # Alpha-beta pruning
        alpha = max(alpha, value['value'])
        if alpha >= beta:
            break

    return value
