def part1(step):
    result, current = [0], 0
    for v in range(1, 2018):
        current = (current + step) % v + 1
        result.insert(current, v)
    return result[current + 1]


def part2(step):
    current = 0
    for v in range(1, 50000001):
        current = (current + step) % v + 1
        if current == 1:
            result = v
    return result


print(part1(366))
print(part2(366))
