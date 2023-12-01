#!/usr/bin/env python3

accum = 0
with open('day1.input') as file:
    for line in file:
        digits = [int(c) for c in line if c.isdigit()]
        if len(digits) < 1:
            continue

        accum += (digits[0] * 10) + digits[-1]

print(accum)

# Part 2

m = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five' : 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def digits_in_line(line):
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(int(line[i]))
            continue

        for k, v in m.items():
            if line[i:].startswith(k):
                digits.append(v)
                break
    return digits

accum = 0
with open('day1.input') as file:
    for line in file:
        digits = digits_in_line(line)
        print(digits)
        if len(digits) < 1:
            continue
        accum += (digits[0] * 10) + digits[-1]

print(accum)


