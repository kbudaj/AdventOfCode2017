def calc(banks):
    states, step, last_state = {}, 0, 0
    while tuple(banks) not in states:
        states[tuple(banks)] = step
        max_i, blocks, step = 0, 0, step + 1

        for i, bank in enumerate(banks):
            if bank == max(banks):
                max_i, blocks = i, bank
                banks[i] = 0
                break

        for offset in range(1, blocks+1):
            banks[(max_i+offset)%len(banks)] += 1
        last_state = tuple(banks)

    return len(states), len(states) - states.get(last_state)

assert calc([0, 2, 7, 0]) == (5, 4)

with open("input.txt", "r") as f:
    inp = list(map(int, f.read().split()))
    print(f'Part 1, Part2: {calc(inp)}')
