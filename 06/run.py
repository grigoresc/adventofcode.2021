import re
from collections import defaultdict

inp = [line.strip() for line in open('input.txt', 'r')]
lanternfish = list(map(int, re.findall(r'\d+', inp[0])))


def Solve(rounds):
    d = defaultdict(int)
    for f in lanternfish:
        d[f] += 1
    for r in range(0, rounds):
        pd = d.copy()
        for i in range(1, 8 + 1):
            d[i - 1] = pd[i]
        d[6] += pd[0]
        d[8] = pd[0]
    l = sum(d.values())
    print(l)


Solve(80)
# 355386
Solve(256)
# 1613415325809
