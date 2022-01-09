input = open('input20.txt').readlines()

algorithm = input[0][:-1]

picture = {}

y = 0
for line in input[2:]:
    x = 0
    for el in line[:-1]:
        picture[(x, y)] = el
        x += 1
    y += 1


def s_to_d(string):
    # string to binary
    binary = ''
    for el in string:
        if el == '.':
            binary += '0'
        if el == '#':
            binary += '1'
    
    # binary to decimal    
    num = 0
    i = 0
    for bit in binary:
        num += int(bit) * (2**(len(binary) - 1 - i))
        i += 1

    return num

def square(point, picture, step):
    x, y = point

    n = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]

    string = ''

    for (xx, yy) in n:
        if (xx, yy) not in picture:
            if step%2 != 0:
                string += '.'
            else:
                string += '#'
        else:
            string += picture[xx, yy]

    return string


def apply(picture, algorithm, step):
    new_picture = {}

    # find min x - max x
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    
    for point in picture.keys():
        if point[0] < min_x:
            min_x = point[0]
        if point[0] > max_x: 
            max_x = point[1]
        if point[1] < min_y:
            min_y = point[0]
        if point[1] > max_y: 
            max_y = point[1]        

    for y in range(min_y-1, max_y+2):
        for x in range(min_x-1, max_x+2):
            sq = square((x, y), picture, step)
            index = s_to_d(sq)
            new_value = algorithm[index]

            new_picture[(x, y)] = new_value


    return new_picture

# part one
step = 1
max_step = 2

while step <= max_step:
    new_picture = apply(picture, algorithm, step)
    picture = new_picture.copy()
    step += 1


print('pixels lit after 2 steps:', list(picture.values()).count('#'))

# part two

picture = {}

y = 0
for line in input[2:]:
    x = 0
    for el in line[:-1]:
        picture[(x, y)] = el
        x += 1
    y += 1

step = 1
max_step = 50

while step <= max_step:
    new_picture = apply(picture, algorithm, step)
    picture = new_picture.copy()
    step += 1

print('pixels lit after 50 steps:', list(picture.values()).count('#'))
