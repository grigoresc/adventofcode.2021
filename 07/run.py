import re
from collections import defaultdict

# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]


def parse(line):
    vals = list(map(int, re.findall(r'\d+', line)))
    print(vals)
    return vals


lst = parse(inp[0])

f = set(lst)
ms = 100000000000000

h = defaultdict(int)


def fib(s):
    if h[s] > 0:
        return h[s]
    a = 0
    for i in range(1, s + 1):
        a += i
    h[s] = a
    return a


for p in range(1, max(f) + 100):
    v = map(lambda x: abs(fib(abs(p - x))), lst)
    s = sum(list(v))
    # print(s, p)
    if s < ms:
        ms = s
print(ms)
