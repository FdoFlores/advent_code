# --- Day 1: Trebuchet?! ---
import re
file = 'day1'
text = []
file = open(f'inputs/{file}.txt', 'r')
data = file.read()
text = data.split("\n")

# text variable its the txt file made list of lines.
# so code goes here

sum = 0

wrote_nums = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
for line in text:
    new_num = '0'
    new_line = ''
    act = line
    for char in line:
        new_line += char
        for num_key, num_val in wrote_nums.items():
            if num_key in new_line:
                new_line = new_line[:-1] + str(num_val) + new_line[-1]

    line = new_line
    line = re.sub(r'[a-zA-z]*', '', line)
    if len(line) > 1:
        new_num = f'{line[0]}{line[-1]}'
    elif len(line) == 1:
        new_num = f'{line}{line}'
    else:
        continue
    sum += int(new_num)

print(sum)