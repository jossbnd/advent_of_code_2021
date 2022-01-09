input = open('input07.txt').readline()

positions = [int(pos) for pos in input.split(',')]

# part 1
def cost_at_x(x):
  cost = 0
  for pos in positions:
    cost += ((x - pos)**2)**0.5
  return int(cost)

cost = cost_at_x(0)
for x in range(min(positions), max(positions)+1):
  if cost_at_x(x) <= cost:
    cost = cost_at_x(x)
    good_pos = x
  else:
    break

print('part one - minimum cost:', cost)

# part 2
def cost_at_x(x):
  cost = 0
  for pos in positions:
    dist_pos = ((x - pos)**2)**0.5
    cost += dist_pos + sum(range(int(dist_pos)))
  return int(cost)

cost = cost_at_x(0)
for x in range(min(positions), max(positions)+1):
  if cost_at_x(x) <= cost:
    cost = cost_at_x(x)
    good_pos = x
  else:
    break

print('part one - minimum cost:', cost)

# optimized
random = 400
cost = cost_at_x(random)
if cost_at_x(random) < cost_at_x(x+1):
  for x in range(random, min(positions)-1, -1):
      if cost_at_x(x) <= cost:
        cost = cost_at_x(x)
        good_pos = x
      else:
        break

if cost_at_x(random) > cost_at_x(x+1):
  for x in range(random, max(positions)+1):
      if cost_at_x(x) <= cost:
        cost = cost_at_x(x)
        good_pos = x
      else:
        break
