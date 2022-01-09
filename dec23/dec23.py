
room_size = 4

# part one
# initial_state = {
#     'hallway': ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     2: ['C', 'D'],
#     4: ['A', 'C'],
#     6: ['B', 'A'],
#     8: ['D', 'B']
#     }

# part two

initial_state = {
    'hallway': ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    2: ['C', 'D', 'D', 'D'],
    4: ['A', 'C', 'B', 'C'],
    6: ['B', 'B', 'A', 'A'],
    8: ['D', 'A', 'C', 'B']
    }

# part one
# goal_state = {
#     'hallway': ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     2: ['A', 'A'],
#     4: ['B', 'B'],
#     6: ['C', 'C'],
#     8: ['D', 'D']   
# }

# part two
goal_state = {
    'hallway': ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    2: ['A', 'A', 'A', 'A'],
    4: ['B', 'B', 'B', 'B'],
    6: ['C', 'C', 'C', 'C'],
    8: ['D', 'D', 'D', 'D']   
}

# test_state = {
#     'hallway': ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     2: ['C', 'D'],
#     4: ['A', 'C'],
#     6: ['B', 'A'],
#     8: ['D', 'B']
#     }

test_state = {
    'hallway': ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    2: ['C', 'A', 'A', 'A'],
    4: ['D', 'B', 'B', 'B'],
    6: ['A', 'C', 'C', 'C'],
    8: ['B', 'D', 'D', 'D']  
    }


def display(state):
    print(''.join(state['hallway']))
    print('##' + state[2][0] + '#' + state[4][0] + '#' + state[6][0] + '#' + state[8][0] + '##')
    print('##' + state[2][1] + '#' + state[4][1] + '#' + state[6][1] + '#' + state[8][1] + '##')


costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

room_of = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

fish_of = {
    2: 'A',
    4: 'B',
    6: 'C',
    8: 'D'
}



def free_rooms(fish, room_size):
    if room_size == 2:
        return [['.', '.'], ['.', fish]]

    if room_size == 4:
        return [['.', '.', '.', '.'], ['.', '.', '.', fish], ['.', '.', fish, fish], ['.', fish, fish, fish]]


def no_block_to_room(spot, state, fish):
    room = room_of[fish]
    if spot < room:
        if state['hallway'][spot+1:room+1] == ['.'] * len(state['hallway'][spot+1:room+1]):
            return True

    if spot > room:
        if state['hallway'][room:spot] == ['.'] * len(state['hallway'][room:spot]):
            return True

    return False


def can_go_in(spot, state):
    fish = state['hallway'][spot]
    if fish in 'ABCD' and state[room_of[fish]] in free_rooms(fish, room_size) and no_block_to_room(spot, state, fish):
        return True

    else:
        return False


def move_in(spot, c, state, room_size):

    new_state = {}

    for key in state.keys():
        new_state[key] = state[key].copy()

    fish = state['hallway'][spot]
    room = room_of[fish]

    new_c = c + ((abs(room - spot) + (room_size - state[room].count(fish))) * costs[fish])

    new_state['hallway'][spot] = '.'

    new_state[room][room_size - state[room].count(fish) - 1] = fish

    return new_c, new_state


def no_block_to_hallway(room, bed, spot, state):
    if spot > room:
        if state['hallway'][room:spot+1] == ['.'] * len(state['hallway'][room:spot+1]):
            return True

    if spot < room:
        if state['hallway'][spot:room+1] == ['.'] * len(state['hallway'][spot:room+1]):
            return True    

    return False



def can_go_out(room, bed, spot, state):
    fish = state[room][bed]

    if fish in 'ABCD':
        if bed == 0 and no_block_to_hallway(room, bed, spot, state) and state[room] not in state[room] != goal_state[room]:
            return True

        if bed != 0 and state[room][bed-1] == '.' and no_block_to_hallway(room, bed, spot, state) and state[room] not in free_rooms(fish_of[room], room_size):
            return True
    return False


def move_out(room, bed, spot, c, state):
    new_state = {}

    for key in state.keys():
        new_state[key] = state[key].copy()

    fish = state[room][bed]

    new_c = c + ((abs(room - spot) + bed + 1) * costs[fish])

    new_state['hallway'][spot] = fish

    new_state[room][bed] = '.'

    return new_c, new_state


def every_possible_states(c, state):
    new_cs = []
    new_states = []
    
    for spot in range(len(state['hallway'])):
        if can_go_in(spot, state):
            new_state = {}
            new_c = 0
            new_c, new_state = move_in(spot, c, state, room_size)

            new_cs.append(new_c)
            new_states.append(new_state)


    for room, bed in [(room, bed) for room in list(state.keys())[1:] for bed in range(room_size)]:
        for spot in [0, 1, 3, 5, 7, 9, 10]:
            if can_go_out(room, bed, spot, state):
                new_state = {}
                new_c = 0
                new_c, new_state = move_out(room, bed, spot, c, state)

                new_cs.append(new_c)
                new_states.append(new_state)

    return list(zip(new_cs, new_states))

# print(test_state)
# print(every_possible_states(0, test_state))
# print(len(every_possible_states(0, test_state)))


from queue import PriorityQueue


def find_min_path(initial_state, goal_state):
    i = 0
    P = PriorityQueue()
    P.put((0, i, initial_state))
    visited = [initial_state]

    while P:
        c, id, state = P.get()

        if state == goal_state:
            return c

        
        # print('1', (c, state))

        if every_possible_states(c, state):
            for cc, possible_state in every_possible_states(c, state):
                if possible_state not in visited:
                    print('2', (cc, possible_state))
                    visited.append(possible_state)
                    i += 1
                    P.put((cc, i, possible_state))


# print('solution part one', find_min_path(initial_state, goal_state))
print('solution part two', find_min_path(initial_state, goal_state))


# print(every_possible_states(9966, {'hallway': ['D', 'B', '.', '.', '.', '.', '.', '.', '.', 'A', 'C'], 2: ['.', 'D'], 4: ['.', 'C'], 6: ['.', 'A'], 8: ['.', 'B']}))

# print('coucou')