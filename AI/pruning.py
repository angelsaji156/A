
import math

nodes_minimax = 0
nodes_ab = 0

# Winning positions
wins = [(0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)]

# Check winner
def winner(board):
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

# Evaluation function
def evaluate(board):
    w = winner(board)
    if w == 'X':
        return 10
    if w == 'O':
        return -10
    return 0

# Minimax algorithm
def minimax(board, is_max):
    global nodes_minimax
    nodes_minimax += 1

    score = evaluate(board)
    if score != 0 or ' ' not in board:
        return score

    best = -math.inf if is_max else math.inf

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X' if is_max else 'O'
            val = minimax(board, not is_max)
            board[i] = ' '

            if is_max:
                best = max(best, val)
            else:
                best = min(best, val)

    return best

# Alpha-Beta Pruning
def alphabeta(board, alpha, beta, is_max):
    global nodes_ab
    nodes_ab += 1

    score = evaluate(board)
    if score != 0 or ' ' not in board:
        return score

    best = -math.inf if is_max else math.inf

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X' if is_max else 'O'
            val = alphabeta(board, alpha, beta, not is_max)
            board[i] = ' '

            if is_max:
                best = max(best, val)
                alpha = max(alpha, best)
            else:
                best = min(best, val)
                beta = min(beta, best)

            if beta <= alpha:
                break

    return best

# Find best move
def best_move(board, use_ab):
    best = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'

            if use_ab:
                val = alphabeta(board, -math.inf, math.inf, False)
            else:
                val = minimax(board, False)

            board[i] = ' '

            if val > best:
                best = val
                move = i

    return move

# Main program
board = ['X','O','X',
         ' ','O',' ',
         ' ',' ',' ']

print("TIC TAC TOE - ALPHA BETA PRUNING")

print("Minimax Best Move:", best_move(board, False))
print("Minimax Nodes:", nodes_minimax)

print("Alpha-Beta Best Move:", best_move(board, True))
print("Alpha-Beta Nodes:", nodes_ab)

reduction = (1 - nodes_ab / nodes_minimax) * 100
print("Pruning Reduction: {:.2f}%".format(reduction))
