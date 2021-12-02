""" Day 2: Dive! """
# PART ONE

with open('inputs/2.txt') as f:
    instr = list(f.readlines())
    
hp = 0
d = 0
for i in instr:
    i_type = i.strip().split(' ')[0]
    i_num = int(i.strip().split(' ')[1])
    if (i_type == 'forward'):
        hp += i_num
    elif (i_type == 'down'):
        d += i_num
    elif (i_type == 'up'):
        d -= i_num

print(hp * d)