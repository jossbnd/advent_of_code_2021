with open('input03.txt') as input_txt:
    input = input_txt.read()

diag = input.split('\n')[:-1]

# part one

gamma = ''
epsilon = ''

for bit in range(len(diag[0])):
    count_0 = 0
    count_1 = 0
    for number in diag:
        if number[bit] == '0':
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(gamma)
print(epsilon)

def bin_to_dec(string):
    power = len(string) - 1
    decimal = 0
    for bit in string:
        decimal += int(bit) * 2 ** power
        power -= 1
    return decimal

gamma_dec = bin_to_dec(gamma)
epsilon_dec = bin_to_dec(epsilon)

print('gamma dec : {}'.format(gamma_dec))
print('espilon dec : {}'.format(epsilon_dec))

print('power consumption: {}'.format(gamma_dec * epsilon_dec))
print('\n')

# part two

# Oxygen
for bit in range(len(diag[0])):
    count_0 = 0
    count_1 = 0
    for number in diag:
        if number[bit] == '0':
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        for number in diag[:]:
            if number[bit] == '1':
                diag.remove(number)
    else:
        for number in diag[:]:
            if number[bit] == '0':
                diag.remove(number)
    if len(diag) == 1:
        oxygen = diag[0]
        break

# Carbon dioxide
diag = input.split('\n')[:-1]

for bit in range(len(diag[0])):
    count_0 = 0
    count_1 = 0
    for number in diag:
        if number[bit] == '0':
            count_0 += 1
        else:
            count_1 += 1
    if count_0 > count_1:
        for number in diag[:]:
            if number[bit] == '0':
                diag.remove(number)
    else:
        for number in diag[:]:
            if number[bit] == '1':
                diag.remove(number)
    if len(diag) == 1:
        co2 = diag[0]
        break

oxygen_dec = bin_to_dec(oxygen)
co2_dec = bin_to_dec(co2)

print('oxygen dec : {}'.format(oxygen_dec))
print('co2 dec : {}'.format(co2_dec))

print('life support rating: {}'.format(oxygen_dec * co2_dec))