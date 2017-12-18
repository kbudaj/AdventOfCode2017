def dance(inp, i=16, times=1):
    p = [chr(a) for a in range(97, 97+i)]
    states = set()

    for t in range(times):
        if tuple(p) in states:
            return dance(inp, times=times%t)
        else:
            states.add(tuple(p))

        for i in inp:
            if i[0] == 's':
                n = int(i.split('s')[1])%len(p)
                for _ in range(n):
                    p = [p[-1]] + p[:-1]
            elif i[0] == 'x':
                a, b = (int(v) for v in i[1:].split('/'))
                p[a], p[b] = p[b], p[a]
            elif i[0] == 'p':
                a, b = i[1:].split('/')
                a_i, b_i = p.index(a), p.index(b)
                p[a_i], p[b_i] = p[b_i], p[a_i]
    return ''.join(p)


assert dance(['s1', 'x3/4', 'pe/b'], 5) == 'baedc'

with open('input.txt', 'r') as f:
    inp = f.read().strip().split(',')

print("Part 1:", dance(inp))
print("Part 2:", dance(inp, times=1000000000))
