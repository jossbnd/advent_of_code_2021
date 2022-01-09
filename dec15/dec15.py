input = open('input15.txt').readlines()

cave = [[int(num) for num in line[:-1]] for line in input]

start = (0, 0)
end = (len(cave[0])-1, len(cave)-1)

adj_cave = {}

for y in range(len(cave)):
  for x in range(len(cave[0])):
    l = []
    weights = []
    for xx, yy in [(x+1, y), (x, y+1)]:
      if xx >= 0 and yy >= 0 and xx < len(cave[y]) and yy < len(cave):
        l.append((xx, yy))
        weights.append(cave[yy][xx])
     
    adj_cave[(x, y)] = {k:v for k, v in zip(l, weights)}

# from collections import deque

from queue import PriorityQueue

def neighbours(coord):
    i, j = coord[0], coord[-1]
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

def find_min_path(cave, start, end):
    P = PriorityQueue()
    P.put((0, start))
    visited = {start, }
    while P:
        r, coord = P.get() 
        if coord == end:
            return r
        
        for n in neighbours(coord):
            if 0 <= n[0] < len(cave) and 0 <= n[-1] < len(cave[0]):
                if n not in visited:
                    visited.add(n)
                    dr = cave[n[1]][n[0]]
                    P.put((r + dr, n))

print('part one lowest risk:', find_min_path(cave, start, end))


# part two

lenght = len(cave)

# enlarge on x
step = 4
for step in range(1, step+1):
  for y in range(0, lenght):
    for x in range(0, lenght):
      if (cave[y][x] + step)%9 == 0:
        cave[y].append(9)
      else:
        cave[y].append((cave[y][x] + step)%9)

# enlarge on y
for step in range(1, step+1):
  for y in range(0, lenght):
    cave.append([(el + step)%9 if (el + step)%9 != 0 else 9 for el in cave[y]])

end = (len(cave[0])-1, len(cave)-1)

print('part one lowest risk:', find_min_path(cave, start, end))


