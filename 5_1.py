""" Day 5: Hydrothermal Venture """
# PART ONE

lines = []
with open('inputs/5.txt') as f:
    for line in f:
        points = line.strip().split(' -> ')
        x1 = int(points[0].split(',')[0])
        y1 = int(points[0].split(',')[1])
        x2 = int(points[1].split(',')[0])
        y2 = int(points[1].split(',')[1])
        lines.append([(x1, y1), (x2, y2)])

map = {}
for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]
    # vertical
    if (x1 == x2):
        min_y = y1
        max_y = y2
        if (y2 < y1):
            min_y = y2
            max_y = y1
        for i in range(min_y, max_y+1):
            point = (x1, i)
            if (point in map):
                map[point] += 1
            else:
                map[point] = 1
    # horizontal
    elif (y1 == y2):
        min_x = x1
        max_x = x2
        if (x2 < x1):
            min_x = x2
            max_x = x1
        for i in range(min_x, max_x+1):
            point = (i, y1)
            if (point in map):
                map[point] += 1
            else:
                map[point] = 1

print(len([ point for point, occ in map.items() if occ >= 2 ]))