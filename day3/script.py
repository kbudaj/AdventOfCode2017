def spiral1():
    up, right, left, down = 0, 0, 0, 0
    pos = {'x': 0, 'y': 0}
    yield pos
    while True:
        while pos['x'] <= right:
            pos['x'] += 1
            yield pos
        right = pos['x']
        while pos['y'] <= up:
            pos['y'] += 1
            yield pos
        up = pos['y']
        while pos['x'] >= left:
            pos['x'] -= 1
            yield pos
        left = pos['x']
        while pos['y'] >= down:
            pos['y'] -= 1
            yield pos
        down = pos['y']

def update_board(board, pos):
    if pos['x'] == 0 and pos['y'] == 0:
        value = 1
    else:
        value = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    value += board[pos['x']+i][pos['y']+j]
                except KeyError:
                    pass
    if pos['x'] not in board.keys():
        board[pos['x']] = {}
    board[pos['x']][pos['y']] = value
    return board

def spiral2():
    up, right, left, down = 0, 0, 0, 0
    board = {}
    pos = {'x': 0, 'y': 0, 'value': 1}
    board = update_board(board, pos)
    yield board[pos['x']][pos['y']]

    while True:
        while pos['x'] <= right:
            pos['x'] += 1
            board = update_board(board, pos)
            yield board[pos['x']][pos['y']]
        right = pos['x']
        while pos['y'] <= up:
            pos['y'] += 1
            board = update_board(board, pos)
            yield board[pos['x']][pos['y']]
        up = pos['y']
        while pos['x'] >= left:
            pos['x'] -= 1
            board = update_board(board, pos)
            yield board[pos['x']][pos['y']]
        left = pos['x']
        while pos['y'] >= down:
            pos['y'] -= 1
            board = update_board(board, pos)
            yield board[pos['x']][pos['y']]
        down = pos['y']

s1 = spiral1()
for i in range(312051):
    pos = next(s1)

steps = abs(pos['x']) + abs(pos['y'])
print(f"Part 1: {steps}")

s2 = spiral2()
while True:
    value = next(s2)
    if value > 312051:
        print(f"Part 2: {value}")
        break





