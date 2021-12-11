""" Day 11: Dumbo Octopus """
# PART ONE
import numpy as np

def evolve(grid):
    w = len(grid[0])
    h = len(grid)
    grid += 1
    fx, fy = np.where(grid > 9)
    
    start = list(zip(fx, fy))
    queue = start
    visited = set()
    while (queue):
        (curr_i, curr_j) = start.pop(0)
        if ( (curr_i, curr_j) in visited ):
            continue
        visited.add( (curr_i, curr_j) )
        grid[curr_i][curr_j] = 0
        # clockwise
        neighbours = [(curr_i-1, curr_j), (curr_i-1, curr_j+1), (curr_i, curr_j+1), (curr_i+1, curr_j+1), 
                      (curr_i+1, curr_j), (curr_i+1, curr_j-1), (curr_i, curr_j-1), (curr_i-1, curr_j-1)]
        
        for n in neighbours:
            x, y = n
            if ( (x,y) in visited ):
                continue
            if (x >= 0 and y >= 0 and x < w and y < h):
                grid[x][y] += 1
                if (grid[x][y] > 9):
                    queue.append( (x, y) )
    
    x0, _ = np.where(grid == 0)
    return (len(x0))

grid = []
with open('inputs/11.txt') as f:
    for line in f:
        grid.append([ int(c) for c in line.strip() ])

grid = np.array(grid)
fc = 0
for step in range(100):
    fc += evolve(grid)  
 
print(fc)