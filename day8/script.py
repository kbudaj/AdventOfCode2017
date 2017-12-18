import operator

ops = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt}

def _condition(operator, arg1, arg2):
    return ops.get(operator)(int(arg1), int(arg2))


def part1_2(imp):
    pattern = ('var', 'instruction', 'value', 'if', 'arg1', 'operator', 'arg2')
    data, highest = {}, 0
    for line in imp:
        i = dict(zip(pattern, line.split()))
        for r in 'var', 'arg1':
            if i[r] not in data:
                data[i[r]] = 0

        if _condition(i['operator'], data[i['arg1']], i['arg2']):
            if i['instruction'] == 'inc':
                data[i['var']] += int(i['value'])
            elif i['instruction'] == 'dec':
                data[i['var']] -= int(i['value'])
            if data[i['var']] > highest:
                highest = data[i['var']]

    return max(data.values()), highest


with open('input1.txt', 'r') as f:
    imp = f.read().splitlines()

print("Part1: {} Part2: {}".format(*part1_2(imp)))

