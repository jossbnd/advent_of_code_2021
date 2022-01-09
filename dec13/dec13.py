input = open('input13.txt').readlines()

dots = [[int(num) for num in line.split(',')] for line in input[:-13]]

folds = [[i if i == 'x' or i == 'y' else int(i) for i in line[11:].split('=')] for line in input[-12:]]

xs = []
ys = []

for dot in dots:
  xs.append(dot[0])
  ys.append(dot[1])

paper = [['.' for x in range(max(xs)+1)] for y in range(max(ys)+1)]

for dot in dots:
  paper[dot[1]][dot[0]] = '#'

# part one

def fold(grid, axis, line):
  if axis == 'x':
    new_grid = [['#' if grid[y][line-x] == '#' or grid[y][line+x] == '#'  else '.' for x in range(1, line+1)] for y in range(len(grid))]
    return new_grid

  if axis == 'y':
    new_grid = [['#' if grid[line - y][x] == '#' or grid[line + y][x] == '#'  else '.' for x in range(len(grid[y]))] for y in range(line, 0, -1)]
    return new_grid

  # fold once and count dots
for folding in folds[:1]:
  paper = fold(paper, folding[0], folding[1])

count = 0
for y in paper:
  for x in y:
    if x == '#':
      count +=1

print('# of dot after 1st fold:', count)

# part two
  #  apply last folds
for folding in folds[1:]:
  paper = fold(paper, folding[0], folding[1])

  # create the result of the projection of paper and read it!
projected_paper = [['.' for x in range(len(paper[y]))] for y in range(len(paper))]

for j in range(len(paper)):
  for i in range(len(paper[j])):
    projected_paper[j][len(paper[j]) - 1 - i] = paper[j][i]

with open('paper13.txt', 'w') as paper_txt:
  for line in paper:
    paper_txt.write(" ".join(line))
    paper_txt.write('\n')

  paper_txt.write('\n')

  for line in projected_paper:
    paper_txt.write(" ".join(line))
    paper_txt.write('\n')

print('Solution part two: open the .txt in the folder')