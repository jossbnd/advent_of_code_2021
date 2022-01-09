input = open('input09.txt').readlines()

map = [[int(num) for num in line[:-1]] for line in input]

# part one

sum = 0
lows = 0

for r in range(len(map)):
    for c in range(len(map[r])):
        count = 0
        l = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for row, col in l:
            try:
                if map[r][c] < map[row][col]:
                    count += 1
            except IndexError:
                count += 1

        if count == 4:
            lows += 1
            sum += map[r][c] + 1
            

print('sum of the low points risks:', sum)
print('# of low points:', lows)

# part two
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == 9:
            map[r][c] = 'X'

with open("test.txt", "w") as output:
    for line in map:
        output.write(str('-'.join([str(num) for num in line])) + '\n')

def dfs(map, r, c, i=[0]):
    map[r][c] = 'X'
    i[0] += 1
    l = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    for row, col in l:
        if row >= 0 and col >= 0 and row < len(map) and col < len(map[row]) and map[row][col] != 'X':
            dfs(map, row, col, i)
    return i[0]

basins = []

for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] != 'X':
            basins.append(dfs(map, r, c, i=[0]))

print('size of 3 largest basins', sorted(basins)[-3:])

product = 1
for size in sorted(basins)[-3:]:
    product *= size

print('product of 3 largest basins is:', product)

