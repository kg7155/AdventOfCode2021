""" Day 13: Transparent Origami """
# PART ONE
import numpy as np

def fold(paper, dir, fold_pos):
    if (dir == 'x'):
        paper = paper.transpose()
    
    idx = fold_pos-1
    for i in range(fold_pos+1, len(paper)):
        paper[idx] += paper[i]
        idx -= 1
    return paper[:int(len(paper)/2), :]

coordinates = []
instructions = []
with open('inputs/13.txt') as f:
    for line in f:
        if (line[0] == '\n'):
            continue
        elif (line[0] == 'f'):
            line_s = line.strip().split(' ')
            dir, n = line_s[2].split('=')
            instructions.append((dir, int(n)))
        else:
            x, y = line.strip().split(',')
            coordinates.append((int(x),int(y)))

h = max(coordinates, key=lambda item:item[1])[1] + 1
w = max(coordinates, key=lambda item:item[0])[0] + 1

paper = np.array([[0] * w] * h)
for x, y in coordinates:
    paper[y][x] = 1

for i in instructions:
    dir = i[0]
    fold_pos = i[1]
    paper = fold(paper, dir, fold_pos)
    print(np.count_nonzero(paper))
    break