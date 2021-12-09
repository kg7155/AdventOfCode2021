""" Day 9: Smoke Basin """
# PART ONE

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

heightmap = []
with open('inputs/9.txt') as f:
    for line in f:
        nums = []
        for c in line.strip():
            nums.append(int(c))
        heightmap.append(nums)

rl = 0
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
       if (is_lowpoint(heightmap, i, j)):
            rl += 1 + heightmap[i][j]
                
print(rl)