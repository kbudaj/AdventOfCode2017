from functools import reduce

def k_hash(inp, l=256):
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

def part1(inp):
    used = 0
    for i in range(128):
        s = inp+'-'+str(i)
        used += bin(int(k_hash(s), 16))[2:].count('1')
    return used

def _get_neighbours(x, y, grid):
    directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
    neighbours = []
    for i,j in directions:
        if x+i in range(len(grid)) and y+j in range(len(grid)) and grid[y+j][x+i]=='1':
            neighbours.append((x+i, y+j))
    return neighbours

def part2(inp):
    grid = []
    groups = 0

    for y in range(128):
        s = inp+'-'+str(y)
        grid.append(''.join([bin(int(c, 16))[2:].zfill(4) for c in k_hash(s)]))

    visited = set()
    for y in range(len(grid)):
        for x in range(len(grid)):
            if (x,y) in visited or grid[y][x] == '0':
                continue
            current = (x, y)
            to_visit = [current]
            while to_visit:
                visited.add(current)
                neighbours = [a for a in _get_neighbours(*current, grid)
                              if a not in visited and a not in to_visit]
                to_visit.extend(neighbours)
                current = to_visit.pop()
            groups += 1
    return groups



#print(part1('amgozmfv'))
print(part2('amgozmfv'))
