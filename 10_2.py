""" Day 10: Syntax Scoring """
# PART TWO

def complete(line):
    closed = [0] * len(line)
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
            closed[i] = 1
            closed[j] = 1
    
    # Get indices of unclosed open characters (ie. idx. of '[' without ']')
    ul = [ ind for ind, x in enumerate(closed) if x == 0 ]
    ul.reverse()
    
    # Get unclosed open characters
    uocl = [ line[c] for c in ul ]
    
    # Calculate completion score
    cs_score = 0
    for uoc in uocl:
        cs_score = cs_score * 5 + cs_scores_dict[uoc]
    
    return cs_score

def is_not_corrupted(line):
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
                    return False
    return True
  
open_chars = ['<', '{', '(', '[']
close_chars = ['>', '}', ')', ']']
cs_scores_dict = {'(': 1, '[': 2, '{': 3, '<': 4}

cs_scores = []
with open('inputs/10.txt') as f:
    for line in f:
        if (is_not_corrupted(line.strip())):
            cs_scores.append(complete(line.strip()))

med_pos = int(len(cs_scores)/2)
print(sorted(cs_scores)[med_pos])