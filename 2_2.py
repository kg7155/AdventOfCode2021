""" Day 2: Dive! """
# PART TWO

with open('inputs/2.txt') as f:
    instr = list(f.readlines())
    
a = 0
hp = 0
d = 0
for i in instr:
    i_type = i.strip().split(' ')[0]
    i_num = int(i.strip().split(' ')[1])
    if (i_type == 'forward'):
        hp += i_num
        d += a * i_num
    elif (i_type == 'down'):
        a += i_num
    elif (i_type == 'up'):
        a -= i_num

print(hp * d)