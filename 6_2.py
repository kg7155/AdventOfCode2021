""" Day 6: Lanternfish """
# PART TWO

with open('inputs/6.txt') as f:
    fish = [ int(t) for t in f.readline().strip().split(',')]
    
fish_count = [0] * 9
for f in fish:
    fish_count[f] += 1

for day in range(256):
    zeroes = fish_count[0]
    for i in range(8):
        fish_count[i] = fish_count[i+1]
    fish_count[8] = zeroes
    fish_count[6] += zeroes

print(sum(fish_count))