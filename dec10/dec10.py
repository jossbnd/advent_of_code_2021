input = open('input10.txt').readlines()

nav = [[chunk for chunk in line[:-1]] for line in input]

# part one

points = {')': 3, ']': 57, '}': 1197, '>': 25137}

closed = [')', ']', '}', '>']
opened = ['(', '[', '{', '<']

sum = 0

for line in nav[:]:
    stop = False
    check = [0] * len(line)
    for i in range(len(line)):
        if line[i] in closed:
            for j in range(i-1, -1, -1):
                if line[j] in opened and check[j] == 1:
                    continue
                elif line[j] in opened and check[j] != 1 and line[j] == opened[closed.index(line[i])]:
                    check[j] = 1
                    break
                elif line[j] in opened and check[j] != 1 and line[j] != opened[closed.index(line[i])]:
                    sum += points[line[i]]
                    stop = True
                    nav.remove(line)
                    break
        if stop:
            break

print('scores of corrupted lines:', sum)

# part two

points = {')': 1, ']': 2, '}': 3, '>': 4}

results = []

for line in nav:
    score = 0
    check = [0] * len(line)
    for i in range(len(line)):
        if line[i] in closed:
            for j in range(i-1, -1, -1):
                if line[j] in opened and check[j] == 1:
                    continue
                elif line[j] in opened and check[j] != 1 and line[j] == opened[closed.index(line[i])]:
                    check[j] = 1
                    break

    for i in range(len(line)-1, -1, -1):
        if line[i] in opened and check[i] == 0:
            score = score*5 + points[closed[opened.index(line[i])]]

    results.append(score)

results.sort()
middle = int((len(results)-1)/2)
print('middle score is:', results[middle])