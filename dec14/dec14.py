with open('input14.txt', 'r') as input_file:
    lines = input_file.read()
    split_lines = lines.split("\n")
    # print(split_lines)

# part one 
polymer = split_lines[0]
new_polymer = polymer

#   store instructions
instructions = {}
for el in split_lines[2:-1]:
    splitted_line = el.split(' -> ')
    key = splitted_line[0] 
    value = splitted_line[1]
    instructions[key] = value

#   create polymer
for step in range(10):
    count = 0
    for i in range(len(polymer) - 1):
        seg = polymer[i:i+2]
        new_polymer = new_polymer[:i + count + 1] + instructions[seg] + new_polymer[i + count + 1:]
        if instructions[seg]:
            count += 1
    polymer = new_polymer

#   count letter in polymer
counting = {}
for letter in list(set(polymer)):
    counting[letter] = polymer.count(letter)

result = max(counting.values()) - min(counting.values())
print('Part one result:', result)


# part two

polymer = split_lines[0]

# create initial pair dictionary
pairs = {}
for i in range(len(polymer) - 1):        
    if polymer[i:i+2] in pairs.keys():
        pairs[polymer[i:i+2]] += 1
    else:
        pairs[polymer[i:i+2]] = 1

new_pairs = {}
for i in range(len(polymer) - 1):        
    if polymer[i:i+2] in new_pairs.keys():
        new_pairs[polymer[i:i+2]] += 1
    else:
        new_pairs[polymer[i:i+2]] = 1

# create initial letter dictionary
letters = {}
for letter in polymer:
    if letter in letters.keys():
        letters[letter] += 1
    else:
        letters[letter] = 1

for step in range(40):
    
    for pair in list(pairs.keys())[:]:
        init_count = pairs[pair]
        new_letter = instructions[pair]
        new_pair1 = pair[0] + new_letter
        new_pair2 = new_letter + pair[1]

        if new_letter in letters.keys():
            letters[new_letter] += init_count
        else:
            letters[new_letter] = init_count

        if new_pair1 in new_pairs.keys():
            new_pairs[new_pair1] += init_count
        else:
            new_pairs[new_pair1] = init_count
    
        if new_pair2 in new_pairs.keys():
            new_pairs[new_pair2] += init_count
        else:
            new_pairs[new_pair2] = init_count
    
        new_pairs[pair] -= init_count
      
    new_pairs = {key:val for key, val in new_pairs.items() if val > 0}
    
    # copy dictionary
    pairs = new_pairs.copy()


result = max(letters.values()) - min(letters.values())
print('Part two result:', result)
