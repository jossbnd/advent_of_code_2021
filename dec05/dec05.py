with open('input05.txt') as input_txt:
    input = input_txt.readlines()

winds = [[[int(num) for num in coord.split(',')] for coord in row.split(' -> ')] for row in input]

# part one & two
diagram = [[0 for i in range(1000)] for j in range(1000)]

for wind in winds:
    # vertical line
    if wind[0][0] == wind[1][0]:
        if wind[0][1] < wind[1][1]:
            for i in range(wind[0][1], wind[1][1]+1):
                diagram[i][wind[0][0]] += 1
        elif wind[0][1] > wind[1][1]:
            for i in range(wind[0][1], wind[1][1]-1, -1):
                diagram[i][wind[0][0]] += 1
    
    # horizontal line
    elif wind[0][1] == wind[1][1]:
        if wind[0][0] < wind[1][0]:
            for i in range(wind[0][0], wind[1][0]+1):
                diagram[wind[0][1]][i] += 1
        elif wind[0][0] > wind[1][0]:
            for i in range(wind[0][0], wind[1][0]-1, -1):
                diagram[wind[0][1]][i] += 1

    # diag line
    if wind[0][0] < wind[1][0] and wind[0][1] > wind[1][1]:
        for i in range(0, wind[1][0] - wind[0][0] + 1):
            diagram[wind[0][1] - i][wind[0][0] + i] += 1
    if wind[0][0] < wind[1][0] and wind[0][1] < wind[1][1]:
        for i in range(0, wind[1][0] - wind[0][0] + 1):
            diagram[wind[0][1] + i][wind[0][0] + i] += 1
    if wind[0][0] > wind[1][0] and wind[0][1] < wind[1][1]:
        for i in range(0, wind[0][0] - wind[1][0] + 1):
            diagram[wind[0][1] + i][wind[0][0] - i] += 1    
    if wind[0][0] > wind[1][0] and wind[0][1] > wind[1][1]:
        for i in range(0, wind[0][0] - wind[1][0] + 1):
            diagram[wind[0][1] - i][wind[0][0] - i] += 1 


count_2 = 0
for line in diagram:
    for num in line:
        if num >= 2:
            count_2 += 1

print('points with 2 or more winds: ', count_2)



