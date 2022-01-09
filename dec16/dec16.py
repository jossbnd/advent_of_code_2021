transmissions = open('input16.txt').readline()

correspondance = {
    '0': '0000',
    '1': '0001',
    '2': '0010', 
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

def hexa_to_bits(string):
    bits = ''
    for letter in string:
        bits += correspondance[letter]
    return bits


def num(string):
    num = 0
    i = 0
    for bit in string:
        num += int(bit) * (2**(len(string) - 1 - i))
        i += 1
    return num

    

test = 'C200B40A82'

bits = hexa_to_bits(test)
versions = []

def read(packet):
    version = num(packet[0:3])
    versions.append(version)
    type = num(packet[3:6])

    single = ''

    if type == 4:
        i = 6
        while True:
            if packet[i] == '1':
                single += packet[i+1:i+5]
                i += 5

            if packet[i] == '0':
                single += packet[i+1:i+5]
                i += 5
                break
        return num(single), len(packet[0:i])
            
    if type != 4:
        sum = 0
        if packet[6] == '0':
            sub_packets_length = num(packet[7:22])
            length = 0
            while length < sub_packets_length:
                s, l = read(packet[22+length:22+sub_packets_length])
                length += l
                sum += s

            return sum, len(packet[0:22+length])

        if packet[6] == '1':
            sub_packets_num = num(packet[7:18])
            n = 0
            length = 0
            while n < sub_packets_num:
                s, l = read(packet[18+length:])
                length += l
                sum += s               
                n += 1

            return sum, len(packet[0:18+length])

read(hexa_to_bits(transmissions))
print('sum of versions:', sum(versions))


# part two


test = '9C0141080250320F1802104A08'

bits = hexa_to_bits(test)
versions = []

packets = []
start = 0

def read(packet):
    version = num(packet[0:3])
    versions.append(version)
    type = num(packet[3:6])

    single = ''

    if type == 4:
        i = 6
        while True:
            if packet[i] == '1':
                single += packet[i+1:i+5]
                i += 5

            if packet[i] == '0':
                single += packet[i+1:i+5]
                i += 5
                break
        return num(single), len(packet[0:i])

# sum
    if type == 0:
        sum = 0
        if packet[6] == '0':
            sub_packets_length = num(packet[7:22])
            length = 0
            while length < sub_packets_length:
                s, l = read(packet[22+length:22+sub_packets_length])
                length += l
                sum += s

            return sum, len(packet[0:22+length])

        if packet[6] == '1':
            sub_packets_num = num(packet[7:18])
            n = 0
            length = 0
            while n < sub_packets_num:
                s, l = read(packet[18+length:])
                length += l
                sum += s               
                n += 1

            return sum, len(packet[0:18+length])

# product
    if type == 1:
        product = 1
        if packet[6] == '0':
            sub_packets_length = num(packet[7:22])
            length = 0
            while length < sub_packets_length:
                s, l = read(packet[22+length:22+sub_packets_length])
                length += l
                product *= s

            return product, len(packet[0:22+length])

        if packet[6] == '1':
            sub_packets_num = num(packet[7:18])
            n = 0
            length = 0
            while n < sub_packets_num:
                s, l = read(packet[18+length:])
                length += l
                product *= s               
                n += 1

            return product, len(packet[0:18+length])

# minimum
    if type == 2:
        lst = []
        if packet[6] == '0':
            sub_packets_length = num(packet[7:22])
            length = 0
            while length < sub_packets_length:
                s, l = read(packet[22+length:22+sub_packets_length])
                length += l
                lst.append(s)

            return min(lst), len(packet[0:22+length])

        if packet[6] == '1':
            sub_packets_num = num(packet[7:18])
            n = 0
            length = 0
            while n < sub_packets_num:
                s, l = read(packet[18+length:])
                length += l
                lst.append(s)               
                n += 1

            return min(lst), len(packet[0:18+length])

# maximum
    if type == 3:
        lst = []
        if packet[6] == '0':
            sub_packets_length = num(packet[7:22])
            length = 0
            while length < sub_packets_length:
                s, l = read(packet[22+length:22+sub_packets_length])
                length += l
                lst.append(s)

            return max(lst), len(packet[0:22+length])

        if packet[6] == '1':
            sub_packets_num = num(packet[7:18])
            n = 0
            length = 0
            while n < sub_packets_num:
                s, l = read(packet[18+length:])
                length += l
                lst.append(s)               
                n += 1

            return max(lst), len(packet[0:18+length])

# greater
    if type == 5:
        lst = []
        if packet[6] == '0':
            sub_packets_length = num(packet[7:22])
            length = 0
            while length < sub_packets_length:
                s, l = read(packet[22+length:22+sub_packets_length])
                length += l
                lst.append(s)

            return 1 if lst[0] > lst[1] else 0, len(packet[0:22+length])

        if packet[6] == '1':
            sub_packets_num = num(packet[7:18])
            n = 0
            length = 0
            while n < sub_packets_num:
                s, l = read(packet[18+length:])
                length += l
                lst.append(s)               
                n += 1

            return 1 if lst[0] > lst[1] else 0, len(packet[0:18+length])

# less
    if type == 6:
        lst = []
        if packet[6] == '0':
            sub_packets_length = num(packet[7:22])
            length = 0
            while length < sub_packets_length:
                s, l = read(packet[22+length:22+sub_packets_length])
                length += l
                lst.append(s)

            return 1 if lst[0] < lst[1] else 0, len(packet[0:22+length])

        if packet[6] == '1':
            sub_packets_num = num(packet[7:18])
            n = 0
            length = 0
            while n < sub_packets_num:
                s, l = read(packet[18+length:])
                length += l
                lst.append(s)               
                n += 1

            return 1 if lst[0] < lst[1] else 0, len(packet[0:18+length])

# equal
    if type == 7:
        lst = []
        if packet[6] == '0':
            sub_packets_length = num(packet[7:22])
            length = 0
            while length < sub_packets_length:
                s, l = read(packet[22+length:22+sub_packets_length])
                length += l
                lst.append(s)

            return 1 if lst[0] == lst[1] else 0, len(packet[0:22+length])

        if packet[6] == '1':
            sub_packets_num = num(packet[7:18])
            n = 0
            length = 0
            while n < sub_packets_num:
                s, l = read(packet[18+length:])
                length += l
                lst.append(s)               
                n += 1
            return 1 if lst[0] == lst[1] else 0, len(packet[0:18+length])

print('transmissions result:', read(hexa_to_bits(transmissions))[0])
