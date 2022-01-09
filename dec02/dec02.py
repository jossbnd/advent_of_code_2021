with open('input02.txt') as input_txt:
    input = input_txt.read()

moves_raw = input.split("\n")[:-1]

moves = [s.split() for s in moves_raw]
for s in moves:
  s[1] = int(s[1])

# 1st part
hor_pos = 0
depth = 0

for move in moves:
  if move[0] == 'forward':
    hor_pos += move[1]
  if move[0] == 'down':
    depth += move[1]  
  if move[0] == 'up':
    depth -= move[1]

print(depth)
print(hor_pos)
print("multiply horizontal pos by depth:", hor_pos*depth)

# 2nd part
hor_pos = 0
depth = 0
aim = 0

for move in moves:
  if move[0] == 'forward':
    hor_pos += move[1]
    depth += aim*move[1]
  if move[0] == 'down':
    aim += move[1]  
  if move[0] == 'up':
    aim -= move[1]

print(depth)
print(hor_pos)
print("multiply horizontal pos by depth:", hor_pos*depth)





