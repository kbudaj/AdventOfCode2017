def canceling(inp):
    while True:
        i = inp.find('!')
        if i == -1:
            break
        inp = inp[:i] + inp[(i+2):]
    return inp

def remove_garbage(inp):
    g_start_pos, count = None, 0
    while True:
        if g_start_pos is None:
            g_start_pos = inp.find('<')
            if g_start_pos == -1:
                break
        else:
            g_end_pos = inp.find('>')
            count += g_end_pos - g_start_pos - 1
            inp = inp[:g_start_pos] + inp[g_end_pos+1:]
            g_start_pos = None
    return inp, count

def calc(inp):
    inp, count = remove_garbage(canceling(inp))

    depth, score = 0, 0
    for c in inp:
        if c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
    return score, count

with open('input.txt', 'r') as f:
    print("Part 1: {} Part 2: {}".format(*calc(f.read())))
