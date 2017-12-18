def load_data(inp):
    data = {}
    for l in inp:
        i, depth = l.replace(' ', '').split(':')
        data[int(i)] = int(depth)
    return data

def scanner_state(r, p):
    if p == 0:
        return True
    if r == 2:
        return p%2 == 0
    return p%((r-1)*2) == 0

def part1(inp):
    data = load_data(inp)
    severity = 0

    for current in range(max(data)+1):
        if current in data and scanner_state(data[current], current):
            severity += data[current]*current
    return severity

def part2(inp):
    data = load_data(inp)
    delay = 0

    while True:
        for current in range(max(data)+1):
            if current in data and scanner_state(data[current], current+delay):
                break
        else:
            return delay
        delay += 1


with open('input2.txt', 'r') as f:
    inp = f.read().splitlines()

print(part1(inp))
print(part2(inp))
