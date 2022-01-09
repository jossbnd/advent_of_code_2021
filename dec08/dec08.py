with open('input08.txt') as input_txt:
    input = input_txt.readlines()

signals = [line.split() for line in input]

# sort signals
for signal in signals:
    for i in range(len(signal)):
        signal[i] = ''.join(sorted(signal[i]))


print('1st signal: ', signals[0])


# part one
def is_in(a, b):
    for letter in a:
        if letter not in b:
            return False
    return True


def find_connection(signal):
    connections = [0] * 10
    # find 1, 4, 7, 8
    for digit in signal[:10]:
        if len(digit) == 2:
            connections[1] = digit
        elif len(digit) == 4:
            connections[4] = digit
        elif len(digit) == 3:
            connections[7] = digit
        elif len(digit) == 7:
            connections[8] = digit

    # find 9, 0, 6, 3
    for digit in signal[:10]:
        # find 9
        if len(digit) == 6 and is_in(connections[1], digit) and is_in(connections[4], digit):
            connections[9] = digit
        # find 0
        elif len(digit) == 6 and is_in(connections[1], digit) and not(is_in(connections[4], digit)):
            connections[0] = digit
        # find 6
        elif len(digit) == 6 and not(is_in(connections[1], digit)) and not(is_in(connections[4], digit)):
            connections[6] = digit
        # find 3
        elif len(digit) == 5 and is_in(connections[1], digit):
            connections[3] = digit        
    
    # find 2, 5
    for digit in signal[:10]:
        # find 5
        if len(digit) == 5 and is_in(digit, connections[6]):
            connections[5] = digit
        # find 2
        if len(digit) == 5 and not(is_in(digit, connections[6])) and not(is_in(connections[1], digit)):
            connections[2] = digit       

    return connections

print('example of connections matrix:', find_connection(signals[0]))


# get output + count
count = 0
for signal in signals:
    for i in range(11, 15):
        for j in range(len(find_connection(signal))):
            if signal[i] == find_connection(signal)[j]:
                signal[i] = j
                if j in [1, 4, 7, 8]:
                    count += 1

print('signal after decoding:', signals[0])
print('# of 1, 4, 7, 8 in signals:', count)


# part two
count = 0
for signal in signals:
    count += int(''.join([str(i) for i in signal[-4:]]))


print('addition of all output values gives:', count)