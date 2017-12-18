import time

def part1_v1(str_list):
    total = 0
    l = len(str_list)
    for i, d in enumerate(str_list):
        next = i+1 if i+1 < l else 0
        if str_list[next] == d:
            total += int(d)
    return total

def part1_v2(str_list):
    l = len(str_list)
    return sum(int(d) for i, d in enumerate(str_list) if d == str_list[i+1 if i+1 < l else 0])

def part2_v1(str_list):
    total = 0
    l = len(str_list)
    k = l/2
    for i, d in enumerate(str_list):
        next = int((i+k)%l if not i+k < l else i+k)
        if str_list[next] == d:
            total += int(d)
    return total

def part2_v2(str_list):
    l = len(str_list)
    return sum(int(d) for i, d in enumerate(str_list) if d == str_list[int((i+l/2)%l)])

def asdfowe(inp, start=1):
    return (sum(int(digit)
            for digit, next_digit in zip(inp, inp[start:] + inp)
            if digit == next_digit))

assert part1_v2('1122') == 3
assert part1_v2('1111') == 4
assert part1_v2('1234') == 0
assert part1_v2('91212129') == 9

assert part2_v2('1212') == 6
assert part2_v2('1221') == 0
assert part2_v2('123425') == 4
assert part2_v2('123123') == 12
assert part2_v2('12131415') == 4

with open('input.txt', 'r') as file:
    input = file.read().strip()
    print(f'Part1_v2: {part1_v2(input)}')
    print(f'Part2_v2: {part2_v2(input)}')

