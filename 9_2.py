""" Day 9: Smoke Basin """
# PART TWO
from functools import reduce

def is_lowpoint(map, i, j):
    is_lower = True
    if (j > 0):
        is_lower &= map[i][j] < map[i][j-1] # l
    if (j < len(map[i])-1):
        is_lower &= map[i][j] < map[i][j+1] # r
    if (i > 0):
        is_lower &= map[i][j] < map[i-1][j] # u
    if (i < len(map)-1):
        is_lower &= map[i][j] < map[i+1][j] # d
    return is_lower

def find_basin(map, i, j):
    start = [(i, j)]
    queue = start
    visited = set()
    while (queue):
        (curr_i, curr_j) = start.pop(0)
        if ( (curr_i, curr_j) in visited or map[curr_i][curr_j] == 9):
            continue
        visited.add((curr_i, curr_j))
        if (curr_j > 0):
            queue.append((curr_i, curr_j-1)) # l
        if (curr_j < len(map[i])-1):
            queue.append((curr_i, curr_j+1)) # r
        if (curr_i > 0):
            queue.append((curr_i-1, curr_j)) # u
        if (curr_i < len(map)-1):
            queue.append((curr_i+1, curr_j)) # d
    return visited

heightmap = []
with open('inputs/9.txt') as f:
    for line in f:
        nums = []
        for c in line.strip():
            nums.append(int(c))
        heightmap.append(nums)

basins_sizes = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
       if (is_lowpoint(heightmap, i, j)):
            basins_sizes.append(len(find_basin(heightmap, i, j)))
                
print(reduce(lambda x, y: x * y, sorted(basins_sizes, reverse=True)[:3]))