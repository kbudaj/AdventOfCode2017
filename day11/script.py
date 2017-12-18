class Hex():
    directions = {
        'n':  (0, +1, -1),
        'ne': (+1, 0, -1),
        'se': (+1, -1, 0),
        's':  (0, -1, +1),
        'sw': (-1, 0, +1),
        'nw': (-1, +1, 0)
    }

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.furthest = 0

    def move(self, direction):
        dx, dy, dz = self.directions.get(direction)
        self.x += dx
        self.y += dy
        self.z += dz

    def move_list(self, directions):
        directions = directions.split(',')
        for d in directions:
            self.move(d)
            if self.distance > self.furthest:
                self.furthest = self.distance

    @property
    def distance(self):
        return (abs(self.x) + abs(self.y) + abs(self.z))//2


with open('input.txt', 'r') as f:
    inp = f.readline().strip()

child = Hex()
child.move_list(inp)
print("Part 1:", child.distance)
print("Part 2:", child.furthest)
