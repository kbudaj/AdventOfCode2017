from collections import Counter

with open('input2.txt', 'r') as f:
    imp = f.read().splitlines()

def find_first(imp):
    a = Counter()
    for line in imp:
        line = line.split(' ')
        line = [k.replace(',', '') for k in line if '(' not in k and '->' not in k]
        a.update(line)
    return a.most_common()[-1]

print(a.most_common()[-1])

