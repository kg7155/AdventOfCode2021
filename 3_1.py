""" Day 3: Binary Diagnostic """
# PART ONE

with open('inputs/3.txt') as f:
    report = f.read().splitlines()

gr = ''
er = ''
for i in range(len(report[0])):
    s = ''
    for number in report:
        s += number[i]
    if (s.count('0') > s.count('1')):
        gr += '0'
        er += '1'
    else:
        gr += '1'
        er += '0'

print(int(gr, 2) * int(er, 2))