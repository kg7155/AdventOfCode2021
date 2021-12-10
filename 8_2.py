""" Day 8: Seven Segment Search """
# PART TWO
from functools import reduce

# Not the nicest solution but it does the job
def decode(input, output):
    id = [ s for s in input.split(' ') ]
    id_lengths = [ len(s) for s in input.split(' ') ]
    
    digit_to_code = dict([(1, ''.join(sorted(id[id_lengths.index(2)]))),
                          (4, ''.join(sorted(id[id_lengths.index(4)]))),
                          (7, ''.join(sorted(id[id_lengths.index(3)]))),
                          (8, ''.join(sorted(id[id_lengths.index(7)])))])
    
    # Decode 6 segment digits in next order: 6, 0, 9
    six_indcs = [i for i, s in enumerate(id_lengths) if s == 6]
    for six_idx in six_indcs:
        if (len(id[six_idx].translate({ord(i): None for i in digit_to_code[1]}))) == 5:
            digit_to_code[6] = ''.join(sorted(id[six_idx]))
            break
    six_indcs.remove(six_idx)
    for six_idx in six_indcs:
        if (len(id[six_idx].translate({ord(i): None for i in digit_to_code[4]}))) == 3:
            digit_to_code[0] = ''.join(sorted(id[six_idx]))
            break
    six_indcs.remove(six_idx)
    digit_to_code[9] = ''.join(sorted(id[six_indcs[0]]))
    
    # Decode 5 segment digits in next order: 5, 3, 2
    five_indcs = [i for i, s in enumerate(id_lengths) if s == 5]
    for five_idx in five_indcs:
        if (len(id[five_idx].translate({ord(i): None for i in digit_to_code[6]}))) == 0:
            digit_to_code[5] = ''.join(sorted(id[five_idx]))
            break
    five_indcs.remove(five_idx)
    for five_idx in five_indcs:
        if (len(id[five_idx].translate({ord(i): None for i in digit_to_code[9]}))) == 0:
            digit_to_code[3] = ''.join(sorted(id[five_idx]))
            break
    five_indcs.remove(five_idx)
    digit_to_code[2] = ''.join(sorted(id[five_indcs[0]]))
    
    # Reverse dict for easier search in next step
    code_to_digit = {}
    for k, v in digit_to_code.items():
        code_to_digit[v] = k
    
    # Calculate output value
    output_val = []
    for digit in output.split(' '):
        sd = ''.join(sorted(digit))
        output_val.append(code_to_digit[sd])
    
    return int(reduce(lambda x, y: str(x) + str(y), output_val))

entries = []
with open('inputs/8.txt') as f:
    for line in f:
        entries.append(line.strip())

output_vals = 0
for entry in entries:
    input, output = entry.split(' | ')
    output_vals += decode(input, output)
    
print(output_vals)