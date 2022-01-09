
grids =[]

with open('input04.txt') as input_txt:
    numbers_txt = input_txt.readline()[:-1]
    grids_txt = input_txt.readlines()[1:-1]

    for row in range(0, len(grids_txt)-6, 6):
        grids.append([[int(num) for num in line.split()] for line in grids_txt[row:row+5]])

numbers = [int(num) for num in numbers_txt.split(',')]

# part one
win_grid = 0

for num in numbers:
# marking numbers
    for grid_num in range(len(grids)):
        for row_num in range(5):
            for num_pos in range(5):
                if grids[grid_num][row_num][num_pos] == num:
                    grids[grid_num][row_num][num_pos] = 'O'

# check if win in line
    for grid_num in range(len(grids)):
        for row_num in range(5):
            if grids[grid_num][row_num].count('O') == 5:
                win_grid = grid_num
                last_number = num

# check if win in column
        for column in range(5):
            col_5 = 0
            for row_num in range(5):
                if grids[grid_num][row_num][column] == 'O':
                    col_5 += 1
            if col_5 == 5:
                win_grid = grid_num
                last_number = num

    if win_grid != 0:
        break

print(last_number)
print(grids[win_grid])

# calculate final score
sum = 0

for line in grids[win_grid]:
    for num in line:
        if type(num) == int:
            sum += num

print('sum of unmarked is:', sum)
print('final_score is:', sum*last_number)


# part two: last to win
win_grids = []
last_numbers = []

for num in numbers:
# marking numbers
    for grid_num in range(len(grids)):
        for row_num in range(5):
            for num_pos in range(5):
                if grids[grid_num][row_num][num_pos] == num:
                    grids[grid_num][row_num][num_pos] = 'O'

# check if win in line, store winning grids, then cross it
    for grid_num in range(len(grids)):
        for row_num in range(5):
            if grids[grid_num][row_num].count('O') == 5:
                win_grids.append(grids[grid_num])
                last_numbers.append(num)
                grids[grid_num] = [['X' for i in range(5)] for j in range(5)]

# check if win in column, store winning grids, then cross it
        for column in range(5):
            col_5 = 0
            for row_num in range(5):
                if grids[grid_num][row_num][column] == 'O':
                    col_5 += 1
            if col_5 == 5:
                win_grids.append(grids[grid_num])
                last_numbers.append(num)
                grids[grid_num] = [['X' for i in range(5)] for j in range(5)]

print('last winning grid:', win_grids[-1])

# calculate final score
sum = 0

for line in win_grids[-1]:
    for num in line:
        if type(num) == int:
            sum += num

print('sum of unmarked is:', sum)
print('final_score is:', sum*last_numbers[-1])