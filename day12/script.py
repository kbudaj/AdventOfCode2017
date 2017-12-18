from time import time

def load_data(inp):
    data = {}
    for line in inp:
        p, neighbours = line.replace(' ', '').split('<->')
        data[p] = {p for p in neighbours.split(',')}
    return data


def part1(data):
    connects = set()
    doesnt_c = set()
    for p in data:
        to_visit = [p]
        visited = set()
        while to_visit:
            if '0' in to_visit:
                connects.add(p)
                break
            current = to_visit.pop()
            visited.add(current)
            to_visit.extend([n for n in data[current]
                         if n not in visited and n not in doesnt_c])
        else:
            doesnt_c.add(p)
    return len(connects)


def part2(data):
    visited = set()
    groups = 0
    for p in data:
        if p in visited:
            continue
        else:
            groups += 1
        to_visit = [p]
        while to_visit:
            current = to_visit.pop()
            visited.add(current)
            to_visit.extend([n for n in data[current] if n not in visited])
    return groups





with open('input2.txt', 'r') as f:
    inp = f.read().splitlines()

data = load_data(inp)
print(part1(data))
print(part2(data))

