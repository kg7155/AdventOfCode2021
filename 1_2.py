""" Day 1: Sonar Sweep """
# PART TWO

with open('inputs/1.txt') as f:
    depths = list(map(int, f.readlines()))
    
c = 0
for i in range(1, len(depths)-2):
    s_curr = depths[i] + depths[i+1] + depths[i+2]
    s_prev = depths[i-1] + depths[i] + depths[i+1]
    if (s_curr > s_prev):
        c += 1

print(c)