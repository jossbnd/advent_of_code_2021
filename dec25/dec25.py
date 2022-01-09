input = open('input25.txt').readlines()

x_max = len(input[0][:-1])
y_max = len(input)

grid = {}

for y in range(len(input)):
    for x in range(len(input[y][:-1])):
        if input[y][:-1][x] != '.':
            grid[(x, y)] = input[y][:-1][x]

def is_there(x, y, grid):
    try:
        grid[(x, y)]
        return True

    except KeyError:
        return False


def can_move(x, y, grid):
    if grid[(x, y)] == '>':
        if x + 1 == x_max and is_there(0, y, grid):
            return False

        elif x + 1 != x_max and is_there(x+1, y, grid):
            return False

        else:
            return True

    if grid[(x, y)] == 'v':
        if y + 1 == y_max and is_there(x, 0, grid):
            return False

        elif y + 1 != y_max and is_there(x, y+1, grid):
            return False

        else:
            return True

def move(type, movers, grid):

    for (x, y) in movers:
        grid.pop((x, y))
        if type == '>':          
            if x+1 == x_max:
                grid[(0, y)] = type
            else:
                grid[(x+1, y)] = type

        if type == 'v':
            if y+1 == y_max:
                grid[(x, 0)] = type
            else:
                grid[(x, y+1)] = type

    return grid


moves = 1
i = 0


while moves != 0:
    moves = 0
    i += 1
    movers = []
    for (x, y) in grid.keys():
        if grid[(x, y)] == '>' and can_move(x, y, grid):
            movers.append((x, y))
            moves += 1
    
    move('>', movers, grid)

    movers = []
    for (x, y) in grid.keys():
        if grid[(x, y)] == 'v' and can_move(x, y, grid):
            movers.append((x, y))
            moves += 1

    move('v', movers, grid)

print('herds stops after:', i, 'steps.')