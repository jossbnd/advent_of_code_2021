input = open('input11.txt').readlines()

octs = [[int(num) for num in line[:-1]] for line in input]

# part one

def flash(r, c, grid, has_flashed):
    l = [(r-1, c), (r-1,c+1), (r, c+1), (r+1, c+1), (r+1, c), (r+1, c-1), (r, c-1), (r-1, c-1)]

    for row, col in l:
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]):
            grid[row][col] += 1
            if grid[row][col] == 10:
                flash(row, col, grid, has_flashed)
    
    has_flashed.append((r, c))

steps = 100
count = 0


for step in range(1, steps+1):
    has_flashed = []
    for r in range(len(octs)):
        for c in range(len(octs[r])):
            octs[r][c] += 1
    
    # check if flash
    for r in range(len(octs)):
        for c in range(len(octs[r])):
            if octs[r][c] > 9 and (r, c) not in has_flashed:
                flash(r, c, octs, has_flashed)

    # set the has_flashed at 0 and count
    for r in range(len(octs)):
        for c in range(len(octs[r])):
            if (r, c) in has_flashed:
                octs[r][c] = 0
                count += 1  

print('number of flashes after {} steps: {}'.format(steps, count))


# part two
octs = [[int(num) for num in line[:-1]] for line in input]
steps = 500

for step in range(1, steps+1):
    count = 0
    has_flashed = []
    for r in range(len(octs)):
        for c in range(len(octs[r])):
            octs[r][c] += 1
    
    # check if flash
    for r in range(len(octs)):
        for c in range(len(octs[r])):
            if octs[r][c] > 9 and (r, c) not in has_flashed:
                flash(r, c, octs, has_flashed)

    # set the has_flashed at 0 and count
    for r in range(len(octs)):
        for c in range(len(octs[r])):
            if (r, c) in has_flashed:
                octs[r][c] = 0
                count += 1
    
    if count == len(octs) * len(octs[0]):
        print('first step they all flash is:', step)
        break
