input = open('input06.txt').readline()

fishes = [int(fish) for fish in input.split(',')]

# part one
count = [0]*9

for fish in fishes:
  count[fish] += 1
print(count)

days = 80 
for day in range(1, days+1):
  mother = count[0]
  count = count[1:] + count[:1]
  count[6] += mother

print('number of fishes after {} days: {}'.format(days, sum(count)))

# part two
count = [0]*9
for fish in fishes:
  count[fish] += 1

days = 256 
for day in range(1, days+1):
  mother = count[0]
  count = count[1:] + count[:1]
  count[6] += mother


print('number of fishes after {} days: {}'.format(days, sum(count)))