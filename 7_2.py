""" Day 7: The Treachery of Whales """
# PART TWO

def calc_fuel(positions, to_pos):
    fuel = 0
    for pos in positions:
        d = abs(pos-to_pos)
        fuel += d*(d+1)/2
    return fuel

with open('inputs/7.txt') as f:
    positions = [ int(t) for t in f.readline().strip().split(',') ]
    
min_pos = min(positions)
max_pos = max(positions)

best_fuel = calc_fuel(positions, min_pos)
for i in range(min_pos+1, max_pos):
    fuel = calc_fuel(positions, i)
    if (fuel < best_fuel):
        best_fuel = fuel

print(int(best_fuel))