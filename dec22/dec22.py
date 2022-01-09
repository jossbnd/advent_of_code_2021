input = open('input22.txt').readlines()

# part one

reboot = {}
for line in input[:20]:
    l = [num[2:].split('..') for num in line[3:].strip().split(',')]
    reboot[tuple([int(el) for couple in l for el in couple])] = 1 if line.split()[0] == 'on' else -1
    

def overlap(cube1, cube2):  
    x = max(cube1[0], cube2[0])
    y = max(cube1[2], cube2[2])
    z = max(cube1[4], cube2[4])
    X = min(cube1[1], cube2[1])
    Y = min(cube1[3], cube2[3])
    Z = min(cube1[5], cube2[5])
    if x <= X and y <= Y and z <= Z:
        return x, X, y, Y, z, Z

def vol(cube):
    return (cube[1]-cube[0]+1)*(cube[3]-cube[2]+1)*(cube[5]-cube[4]+1)

import collections
cubes = collections.Counter()

for new_cube, new_sgn in reboot.items():
    update = {}

    update = collections.Counter()

    for old_cube, old_sgn in cubes.items():
        ol = overlap(new_cube, old_cube)
        if ol:
            update[ol] -= old_sgn

    if new_sgn > 0:
        update[new_cube] += new_sgn

    cubes.update(update)

sum = 0
for cube, sgn in cubes.items():
    sum += vol(cube) * sgn

print('part one - # cubes on:', sum)

# part two

reboot = {}
for line in input:
    l = [num[2:].split('..') for num in line[3:].strip().split(',')]
    reboot[tuple([int(el) for couple in l for el in couple])] = 1 if line.split()[0] == 'on' else -1


cubes = collections.Counter()

for new_cube, new_sgn in reboot.items():
    update = {}

    update = collections.Counter()

    for old_cube, old_sgn in cubes.items():
        ol = overlap(new_cube, old_cube)
        if ol:
            update[ol] -= old_sgn

    if new_sgn > 0:
        update[new_cube] += new_sgn

    cubes.update(update)

sum = 0
for cube, sgn in cubes.items():
    sum += vol(cube) * sgn

print('part two - # cubes on:', sum)
