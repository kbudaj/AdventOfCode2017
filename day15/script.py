def g(value, factor):
    last_v = value
    while True:
        last_v = (last_v * factor) % 2147483647
        yield bin(last_v)[2:].zfill(32)[-16:]

def part1():
    gen_a = g(873, 16807)
    gen_b = g(583, 48271)
    counter = 0
    for i in range(40000000):
        if i%1000000 == 0:
            print(str(i//1000000) + '/40')
        if next(gen_a) == next(gen_b):
            counter += 1
    return counter

def g2(value, factor, d):
    last_v = value
    while True:
        last_v = (last_v * factor) % 2147483647
        if last_v % d == 0:
            yield bin(last_v)[2:].zfill(32)[-16:]

def part2():
    gen_a = g2(873, 16807, 4)
    gen_b = g2(583, 48271, 8)
    pair = []
    counter = 0
    for i in range(5000000):
        if i % 1000000 == 0:
            print(str(i//1000000) + '/5')
        if next(gen_a) == next(gen_b):
            counter += 1
    return counter

print("Part1: ", part1())
print("Part2: ", part2())
