""" Day 4: Giant Squid """
# PART TWO
import numpy as np

def mark(drawn, board):
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if (board[row][col][0] == drawn):
                board[row][col][1] = 1

def check_for_win(board):
    row_sum = 0
    for row in board:
        row_sum = sum(f for _, f in row)
        if (row_sum == len(row)):
            return True
    
    board = np.transpose(board, axes=(1,0,2))
    col_sum = 0
    for row in board:
        col_sum = sum(f for _, f in row)
        if (col_sum == len(row)):
            return True
    
    return False

boards = []
pp = []
with open('inputs/4.txt') as f:
    row = f.readline().strip().split(',')
    drawn = [int(s) for s in row if s.isdigit()]
    f.readline()
    for line in f:
        if (line == '\n'):
            boards.append(pp)
            pp = []
        else:
            row = line.strip().split(' ')
            numbers = [int(s) for s in row if s.isdigit()]
            pp.append([[num, 0] for num in numbers])
    else:
        boards.append(pp)

ranks = [ [i, 0] for i in range(len(boards))]
rank = 1
is_last = False
for d in drawn:
    for b in range(0, len(boards)):
        mark(d, boards[b])
        is_won = check_for_win(boards[b])
        if (is_won and ranks[b][1] == 0):
            ranks[b][1] = rank
            if (rank == len(boards)):
                is_last = True
            rank += 1
        if (is_last):
            unmarked_sum = 0
            for row in range(0, len(boards[b])):
                for col in range(0, len(boards[b][0])):
                    if (boards[b][row][col][1] == 0):
                        unmarked_sum += boards[b][row][col][0]
            print (unmarked_sum * d)
            break
    if (is_last):
            break