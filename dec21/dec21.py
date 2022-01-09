player_one = 8
player_two = 3

score_one = 0
score_two = 0

board = list(range(1, 11))

print(board)

def roll(sides, counter=[0]):
    
    sum = 0

    for i in range(3):
        if counter[0] >= 100:
            counter[0] = 1
        else:
            counter[0] += 1

        sum += counter[0]        

    return sum



def move(position, board, dice):

    new_position = position

    for i in range(dice):
        if new_position >= len(board):
            new_position = 1
        else:
            new_position += 1        

    return new_position

counter = [0]
rolls = 0




while True:
    roll_one = roll(100, counter)
    player_one = move(player_one, board, roll_one)
    score_one += player_one
    rolls += 3
    
    if score_one >= 1000:
        break
    
    roll_two = roll(100, counter)
    player_two = move(player_two, board, roll_two)
    score_two += player_two
    rolls += 3

    if score_two >= 1000:
        break


print('#rolls times losing score:', min(score_one, score_two)*rolls)

# part two

from functools import lru_cache
@lru_cache(maxsize=None)

def play(p1, s1, p2, s2):
    p1_initial = p1
    s1_inital = s1

    w1, w2 = 0, 0

    for r in [i+j+k for i in (1, 2, 3) for j in (1, 2, 3) for k in (1, 2, 3)]:
        p1 = (p1_initial + r - 1)%10 + 1
        s1 = s1_inital + p1

        if s1 >= 21:
            w1 += 1
        
        else:
            ww2, ww1 = play(p2, s2, p1, s1)
            w1, w2 = w1 + ww1, w2 + ww2

    return w1, w2

print('# of univers winner wins:', max(play(8, 0, 3, 0)))