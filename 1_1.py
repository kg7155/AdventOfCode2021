""" Day 1: Sonar Sweep """
# PART ONE

with open('inputs/1.txt') as f:
    depths = list(map(int, f.readlines()))
    
c = 0
for i in range(1, len(depths)):
    if (depths[i] > depths[i-1]):
        c += 1
    
print(c)