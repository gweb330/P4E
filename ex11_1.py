
import re

sum = 0

file = open('assignment_data.txt', 'r')
for line in file:
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        for number in numbers:
            sum += int(number)

print(sum)
