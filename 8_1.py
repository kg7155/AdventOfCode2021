""" Day 8: Seven Segment Search """
# PART ONE

outputs = []
with open('inputs/8.txt') as f:
    for line in f:
        outputs.append(line.strip().split(' | ')[1])
    
c = 0
for output in outputs:    
    c += sum([ 1 if len(s) in (2, 3, 4, 7) else 0 for s in output.split(' ') ])

print(c)