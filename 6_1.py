""" Day 6: Lanternfish """
# PART ONE

with open('inputs/6.txt') as f:
    fish = [ int(t) for t in f.readline().strip().split(',')]
    
for day in range(80):
    for f in range(len(fish)):
        fish[f] -= 1
        if (fish[f] == -1):
            fish[f] = 6
            fish.append(8)
    
print(len(fish))