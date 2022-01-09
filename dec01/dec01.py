with open('input01.txt') as input_txt:
  input = input_txt.read()

sonar = [int(n) for n in input.split()]

# increased value
count = 0
for i in range(1, len(sonar)):
  if sonar[i] > sonar[i-1]:
    count += 1
print('# of increased values:', count)


# increased sliding window of 3
count_window = 0
for i in range(1, len(sonar)-2):
  count_prev = sum(sonar[i-1:i+2])
  count_cur = sum(sonar[i:i+3])
  if count_cur > count_prev:
    count_window += 1

print('# of increased sliding values:', count_window)


