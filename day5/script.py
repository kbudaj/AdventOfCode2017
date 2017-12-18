def part1(maze):
    i = 0
    counter = 0
    while i >= 0 and i < len(maze):
        new_i = i + maze[i]
        maze[i] += 1
        i = new_i
        counter += 1
    return counter

assert part1([0, 3, 0, 1, -3]) == 5

def part2(maze):
    i = 0
    counter = 0
    while i >= 0 and i < len(maze):
        new_i = i + maze[i]
        maze[i] = maze[i]-1 if maze[i] >= 3 else maze[i]+1
        i = new_i
        counter += 1
    return counter


assert part2([0, 3, 0, 1, -3]) == 10


with open('input.txt', 'r') as f:
    f = list(map(int, f.read().splitlines()))
    print(part2(f))


