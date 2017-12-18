from functools import reduce


def part1(inp, l=256):
    a = list(range(0, l))
    skip, pos = 0, 0
    for length in inp:
        selected = [a[i%l] for i in range(pos, pos+length)][::-1]
        for v, _ in enumerate(selected):
            a[(pos+v)%l] = selected[v]
        pos += length+skip
        skip +=1
    return a[0] * a[1]

assert part1([3, 4, 1, 5], 5) == 12

def part2(inp, l=256):
    inp = [ord(str(char)) for char in inp] + [17, 31, 73, 47, 23]
    a = list(range(0, l))

    skip, pos = 0, 0
    for _ in range(64):
        for length in inp:
            selected = [a[i%l] for i in range(pos, pos+length)][::-1]
            for v, _ in enumerate(selected):
                a[(pos+v)%l] = selected[v]
            pos += length+skip
            skip +=1

    dense = [a[i*16:i*16+16] for i in range(16)]
    dense = [reduce((lambda x, y: x^y), block) for block in dense]
    return ''.join([format(i, '02x') for i in dense])

assert part2('') == 'a2582a3a0e66e6e86e3812dcb672a272'
assert part2('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
assert part2('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
assert part2('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'

with open('input.txt', 'r') as f:
    inp = f.readline().strip()
    print("Part 1:", part1(map(int, inp.split(','))))
    print("Part 2:", part2(inp))
