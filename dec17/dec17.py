input = (155, 215, -132, -72)

target_x = range(155, 216)
target_y = range(-132, -71)

start = (0, 0)

# part one

def shoot(point, x, y):
    if point[0] in target_x and point[1] in target_y:
        return 'touched!'

    if point[0] >= target_x[-1] or point[1] <= target_y[0]:
        return 'missed!'

    new_point = (point[0] + x, point[1] + y)
    new_x = x - 1 if x > 0 else 0
    new_y = y - 1

    return shoot(new_point, new_x, new_y)

ys = []

x_max = target_x[-1]
x_min = 0
y_max = abs(target_y[0])
y_min = target_y[0] - 1

print(x_max, x_min, y_max, y_min)


for x in range(x_max, x_min, -1):
    for y in range(y_max, 0, -1):
        if shoot(start, x, y) == 'touched!':
            ys.append(y)
y = max(ys)

max_y = 0
while y > 0:
    max_y += y
    y -= 1

print('max height for a succesfull shot:', max_y)

# part two

def shoot(point, x, y):
    if point[0] in target_x and point[1] in target_y:
        return 1

    if point[0] > target_x[-1] or point[1] < target_y[0]:
        return 0

    new_point = (point[0] + x, point[1] + y)
    new_x = x - 1 if x > 0 else 0
    new_y = y - 1

    return shoot(new_point, new_x, new_y)

vels = 0

for x in range(x_max, x_min, -1):
    for y in range(y_max, y_min, -1):
        vels += shoot(start, x, y)

print('# of possible velocities for good shot:', vels)
