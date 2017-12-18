import time

def part1(input):
    checksum = 0
    for line in input:
        line = list(map(int, line.split()))
        checksum += max(line) - min(line)
    return checksum

input = ['5 1 9 5', '7 5 3', '2 4 6 8']
assert part1(input) == 18

def part2(input):
    checksum = 0
    for line in input:
        line = list(map(int, line.split()))
        value = 0
        for i, a in enumerate(line):
            for b in line[i+1:]:
                if a%b == 0:
                    checksum += a/b
                    break
                if b%a == 0:
                    checksum += b/a
                    break
            else:
                continue
            break
    return int(checksum)

input = ['5 9 2 8', '9 4 7 3', '3 8 6 5']
assert part2(input) == 9


with open('input.txt', 'r') as file:
    input = file.read().split('\n')
    print(f'Part1: {part1(input)}')
    print(f'Part2: {part2(input)}')
