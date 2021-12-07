import re
from collections import defaultdict

# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]


def parse(line):
    vals = list(map(int, re.findall(r'\d+', line)))
    return vals


lst = parse(inp[0])
f = set(lst)
dist = defaultdict(int)


def cost(d):
    if dist[d] > 0:
        return dist[d]
    a = 0
    for i in range(1, d + 1):
        a += i
    dist[d] = a
    return a


ms = 100000000000000
for p in range(min(f), max(f)):
    s = sum(map(lambda x: abs(p - x), lst))
    if s < ms:
        ms = s
print(ms)
# 340052

ms = 100000000000000
for p in range(min(f), max(f)):
    s = sum(map(lambda x: cost(abs(p - x)), lst))
    if s < ms:
        ms = s
print(ms)
# 92948968
