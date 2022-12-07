from utils import terminal, actions, move, undo, score


def negascout(grid, depth, alpha, beta, color):
    # Return the maximum value a player can obtain at each step
    if terminal(grid):
        return {'value': score(grid, depth, color)}

    b = beta
    value = None
    for i, action in enumerate(actions(grid)):
        row, col = action

        # Update grid
        move(grid, row, col, color)

        # Calculate maximum value for this action
        ns = negascout(grid, depth + 1, -b, -alpha, -color)
        ns['value'] = -ns['value']

        if alpha < ns['value'] < beta and i > 0:
            # Re-search
            ns = negascout(grid, depth + 1, -beta, -alpha, -color)
            ns['value'] = -ns['value']

        ns['row'] = row
        ns['col'] = col

        # Undo the move
        undo(grid, action[0], action[1])

        # Update the value
        value = ns if value is None else max(value, ns, key=lambda d: d['value'])

        # Alpha-beta pruning
        alpha = max(alpha, value['value'])
        if alpha >= beta:
            break

        b = alpha + 1

    return value
