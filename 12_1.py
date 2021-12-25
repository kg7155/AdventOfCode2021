""" Day 12: Passage Pathing """
# PART ONE

def traverse(cave):
    global current_path
    for node in cave:
        if node.islower() and node in current_path:
            continue
        elif node == 'end':
            current_path.append(node)
            path.append(current_path[:])
            current_path.pop()
        else:
            current_path.append(node)
            traverse(cavemap[node])
    current_path.pop()

cavemap = {}
with open('inputs/12.txt') as f:
    for line in f:
        node_from, node_to = line.strip().split('-')
        if (node_from in cavemap):
            cavemap[node_from].append(node_to)
        else:
            cavemap[node_from] = [node_to]
        if (node_to in cavemap):
            cavemap[node_to].append(node_from)
        else:
            cavemap[node_to] = [node_from]

path = []    
current_path = ['start']
traverse(cavemap['start'])

print(len(path))