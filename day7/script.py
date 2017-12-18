from collections import Counter
import re

def find_first(imp):
    a = Counter()
    for line in imp:
        line = line.split(' ')
        line = [k.replace(',', '') for k in line if '(' not in k and '->' not in k]
        a.update(line)
    return a.most_common()[-1][0]


def load_data(imp):
    data = {}
    pattern = '(?P<name>[^\s]+).(\((?P<weight>\d+)\))(.(->).(?P<neighbours>.+))?'

    for line in imp:
        line = re.match(pattern, line)
        neighbours = None
        if line.group('neighbours'):
            neighbours = line.group('neighbours').replace(',', '').split()
        data[line.group('name')] = {
            'weight': int(line.group('weight')),
            'neighbours': neighbours
        }
    return data


def count_weight(node):
    if data[node]['neighbours'] is None:
        return data[node]['weight'], ([], data[node]['weight'])

    neighbours_data = [count_weight(node) for node in data[node]['neighbours']]
    weight = [weight for weight, _ in neighbours_data]

    if len(set(weight)) != 1:
        values = Counter([weight for weight, _ in neighbours_data]).most_common()
        expected = values[0][0]
        bad = values[-1][0]
        bad_data = [k for i, k in neighbours_data if i == bad][0]

        result = expected - sum(bad_data[0])
        print(f"First anomaly: {result}")

    return data[node]['weight']+sum(weight), (weight, data[node]['weight'])



with open('input2.txt', 'r') as f:
    imp = f.read().splitlines()

first = find_first(imp)
data = load_data(imp)
count_weight(first)
