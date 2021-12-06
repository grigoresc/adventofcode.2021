import re
from collections import defaultdict


def parse(line):
    (x1, y1, x2, y2) = list(map(int, re.findall(r'\d+', line)))
    return x1, y1, x2, y2


def part1():
    for x1, y1, x2, y2 in vents:
        if x1 == x2:
            incy = 1 if y1 < y2 else -1
            for y in range(y1, y2 + incy, incy):
                d[(x1, y)] += 1
        if y1 == y2:
            incx = 1 if x1 < x2 else -1
            for x in range(x1, x2 + incx, incx):
                d[(x, y1)] += 1


def part2():
    for x1, y1, x2, y2 in vents:
        if abs(x2 - x1) == abs(y2 - y1):
            incx = 1 if x1 < x2 else -1
            incy = 1 if y1 < y2 else -1
            for x, y in zip(range(x1, x2 + incx, incx), range(y1, y2 + incy, incy)):
                d[(x, y)] += 1


# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]

vents = list(map(parse, inp))
d = defaultdict(int)

part1()
sln1 = list(filter(lambda x: x > 1, d.values()))
print(len(sln1))
# 5442

part2()
sln2 = list(filter(lambda x: x > 1, d.values()))
print(len(sln2))
# 19571
