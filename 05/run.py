import re


def Parse():
    # inp = [line.strip() for line in open('sample.txt', 'r')]
    inp = [line.strip() for line in open('input.txt', 'r')]

    for l in inp:
        (x1, y1, x2, y2) = list(map(int, re.findall(r'\d+', l)))
        yield (x1, y1, x2, y2)


vents = list(Parse())
c = set()  # covered
c2 = set()  # covered at least two times


def Add(x, y):
    global c, c2
    if (x, y) in c:
        c2.add((x, y))
    else:
        c.add((x, y))


def Part1(vents):
    for x1, y1, x2, y2 in vents:
        if x1 == x2:
            incy = 1 if y1 < y2 else -1
            for y in range(y1, y2+incy, incy):
                Add(x1, y)
        if y1 == y2:
            incx = 1 if x1 < x2 else -1
            for x in range(x1, x2+incx, incx):
                Add(x, y1)


def Part2(vents):
    for x1, y1, x2, y2 in vents:
        if abs(x2-x1) == abs(y2-y1):
            incx = 1 if x1 < x2 else -1
            incy = 1 if y1 < y2 else -1
            y = y1
            for x in range(x1, x2+incx, incx):
                Add(x, y)
                y += incy


Part1(vents)
print(len(c2))
# 5442

Part2(vents)
print(len(c2))
# 19571
