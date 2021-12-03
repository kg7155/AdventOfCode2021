""" Day 3: Binary Diagnostic """
# PART TWO

def eliminate(list, cat):
    for i in range(len(list[0])):
        if (len(list) == 1):
            break      
        s = ''
        for number in list:
            s += number[i]  
        zeroes = s.count('0')
        ones = s.count('1')    
        if (cat == 'most'):
            if (ones >= zeroes):    
                list = [ num for num in list if num[i] == '1' ]
            else:
                list = [ num for num in list if num[i] == '0' ]
        elif (cat == 'least'):
            if (zeroes <= ones):
                list = [ num for num in list if num[i] == '0' ]
            else:
                list = [ num for num in list if num[i] == '1' ]                 
    return list

with open('inputs/3.txt') as f:
    report = f.read().splitlines()

ogr = report.copy()
co2sr = report.copy()

ogr = eliminate(ogr, 'most')
co2sr = eliminate(co2sr, 'least')

print(int(ogr[0], 2) * int(co2sr[0], 2))