input = open('input18.txt').readlines()

lists = [line[:-1] for line in input]

test1 = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
test2 = '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]'

def addition(n1, n2):
    return '[' + n1 + ',' + n2 + ']'

sum = (addition(test1, test2))

from math import *

def explode(sum, i):
    stop1 = 0
    left = 0
    stop2 = 0
    stop3 = 0
    right = 0
    stop4 = 0

    for j in range(i-1, -1, -1):
        if sum[j] in '0123456789':
            left = j
            break
    
    if left > 0:
        for j in range(left-1, -1, -1):
            if sum[j] not in '0123456789':
                stop1 = j
                break

    for j in range(i+1, len(sum)):
        if sum[j] not in '0123456789':
            stop2 = j
            break
    
    for j in range(stop2, len(sum)):
        if sum[j] not in '0123456789':
            stop3 = j
            break
    
    for j in range(stop3+1, len(sum)):
        if sum[j] not in '0123456789':
            stop3 = j
            break
            
    for j in range(stop3, len(sum)):
        if sum[j] in '0123456789':
            right = j
            break
    
    if right > 0:
        for j in range(right+1, len(sum)):
            if sum[j] not in '0123456789':
                stop4 = j
                break

    # explode
    if left == 0:
        return sum[:i-1] + '0' + sum[stop3+1:right] + str(int(sum[stop2+1:stop3]) + int(sum[right:stop4])) + sum[stop4:]

    if right == 0:
        return sum[:stop1+1] + str(int(sum[stop1+1:left+1]) + int(sum[i:stop2])) + sum[left+1:i-1] + '0' + sum[stop3+1:]

    if left != 0 and right != 0:
        return sum[:stop1+1] + str(int(sum[stop1+1:left+1]) + int(sum[i:stop2])) + sum[left+1:i-1] + '0' + sum[stop3+1:right] + str(int(sum[stop2+1:stop3]) + int(sum[right:stop4])) + sum[stop4:]


def reduce(sum):
    # print(sum)
    actions = True
    while actions:
        # print(sum)
        actions = False
        open = 0
        for i in range(len(sum)-1):
            # follow bracket
            if sum[i] == '[':
                open += 1
            if sum[i] == ']':
                open -= 1


            # explode

            if sum[i] in '0123456789' and open >=5:
                sum = explode(sum, i)
                actions = True
                break
            
        if actions == True:
            continue

        for i in range(len(sum)-1):
        # 10 or greater
            if sum[i] in '0123456789' and sum[i+1] in '0123456789':
                sum = sum[:i] + '[' + str(floor((int(sum[i] + sum[i+1]))/2)) + ',' + str(ceil((int(sum[i] + sum[i+1]))/2)) + ']' + sum[i+2:]
                actions = True
                break

    return sum

sum = lists[0]

for line in lists[1:]:
    sum = reduce(addition(sum, line))

def magnitude(sum):
    
    if len(sum) <= 4:
        return int(sum)
    
    for i in range(len(sum)):

        if sum[i] in '0123456789':
            comma = 0
            open_b = len(sum) + 1
            close_b = 0

            for j in range(i+1, len(sum)):
                if sum[j] == ',':
                    comma = j
                    break
            for j in range(i+1, len(sum)):
                if sum[j] == '[':
                    open_b = j
                    break

            for j in range(i+1, len(sum)):
                if sum[j] == ']':
                    close_b = j
                    break
            
            if open_b < close_b:
                    continue
            
            elif open_b > close_b:
                sum = magnitude(sum[:i-1] + str(int(sum[i:comma])*3 + int(sum[comma+1:close_b])*2) + sum[close_b+1:])

            if type(sum) == int:
                return sum

print('magnitude of sum:', magnitude(sum))

# part two

max = 0

for line1 in lists:
    for line2 in lists:
        if line1 != line2:
            add = addition(line1, line2)
            mag = magnitude(reduce(add))
            if mag > max:
                max = mag


print('max magnitude with two lines:', max)