input = open('input12.txt').readlines()

caves = [line[:-1].split('-') for line in input]
print(caves)

# part one

def find_path(cave, caves, smalls, i=[0]):
    if cave.lower() == cave:
        smalls.append(cave) 

    for entry in caves:
        if entry[0] == cave and entry[1] != 'end' and entry[1] != 'start' and entry[1] not in smalls:
            find_path(entry[1], caves, smalls, i)
        elif entry[1] == cave and entry[0] != 'end' and entry[0] != 'start' and entry[0] not in smalls:
            find_path(entry[0], caves, smalls, i)
        elif entry[0] == cave and entry[1] == 'end':
            i[0] += 1
        elif entry[1] == cave and entry[0] == 'end':
            i[0] += 1

    if cave.lower() == cave:
        smalls.remove(cave)

sum = 0

for entry in caves:
    if entry[0] == 'start':
        j = [0]
        find_path(entry[1], caves, smalls=[], i=j)
        sum += j[0]
    if entry[1] == 'start':
        j = [0]
        find_path(entry[0], caves, smalls=[], i=j)
        sum += j[0]

print('part one - # of possible paths:', sum)

# part two

def find_path(cave, caves, smalls, i=[0], visited_twice=[]):
    if cave in smalls:
        visited_twice.append(cave)
    
    if cave.lower() == cave and cave not in smalls:
        smalls.append(cave) 

    for entry in caves:
        if entry[0] == cave and entry[1] != 'end' and entry[1] != 'start' and ((entry[1] not in smalls) or (entry[1] in smalls and len(visited_twice) == 0)):
            find_path(entry[1], caves, smalls, i, visited_twice)
        elif entry[1] == cave and entry[0] != 'end' and entry[0] != 'start' and ((entry[0] not in smalls) or (entry[0] in smalls and len(visited_twice) == 0)):
            find_path(entry[0], caves, smalls, i, visited_twice)
        elif entry[0] == cave and entry[1] == 'end':
            i[0] += 1
        elif entry[1] == cave and entry[0] == 'end':
            i[0] += 1

    if cave.lower() == cave and cave not in visited_twice:
        smalls.remove(cave)

    if cave.lower() == cave and cave in visited_twice:
        visited_twice.remove(cave)
       
sum = 0

for entry in caves:
    if entry[0] == 'start':
        j = [0]
        find_path(entry[1], caves, smalls=[], i=j, visited_twice=[])
        sum += j[0]
    if entry[1] == 'start':
        j = [0]
        find_path(entry[0], caves, smalls=[], i=j, visited_twice=[])
        sum += j[0]

print('part two - # of possible paths:', sum)