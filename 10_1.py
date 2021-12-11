""" Day 10: Syntax Scoring """
# PART ONE

def check(line):
    for i in range(len(line)):
        c = line[i]
    
        if (c in close_chars):
            idx = close_chars.index(c)
            open_char = open_chars[idx]

            close_counter = 0
            for j in range(i-1, -1, -1):
                if (line[j] == c):
                    close_counter += 1
                elif (line[j] == open_char):
                    close_counter -= 1
                    if (close_counter < 0):
                        break
            
            list_to_check = line[j:i+1]
            chars = { k : 0 for k in open_chars + close_chars }
            for cc in list_to_check:
                chars[cc] += 1
            # list of occurences in next order: < { ( [, or > } ) ]
            opening = [ c for (_,c) in [ (k, c) for k, c in chars.items() if k in ('<', '{', '(', '[') ] ]  
            closing = [ c for (_,c) in [ (k, c) for k, c in chars.items() if k in ('>', '}', ')', ']') ] ]  
            
            if (closing[idx] >= opening[idx]):
                if sum([a_i - b_i for a_i, b_i in zip(opening, closing)]) > 0:
                    return se_scores[c]
    return 0
  
open_chars = ['<', '{', '(', '[']
close_chars = ['>', '}', ')', ']']
se_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

se_sum = 0
with open('inputs/10.txt') as f:
    for line in f:
        se_sum += check(line.strip())
        
print(se_sum)