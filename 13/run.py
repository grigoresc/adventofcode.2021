from functools import reduce

# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]


def parse(inp):
    p = set()  # points
    for idx, l in enumerate(inp):
        if len(l) == 0:
            break
        (x, y) = l.split(',')
        p.add((int(x), int(y)))
    f = []  # folds
    for l in inp[idx + 1:]:
        (t, fs) = l.split('=')
        (x, y) = (0, 0)
        if 'y' in t:
            y = fs
        else:
            x = fs
        f.append((int(x), int(y)))
    return p, f


def printmatrix(lst):
    for line in lst:
        s = reduce(lambda x, y: x + y, line, "")
        print(s)


def printp(p):
    maxx = max(list(p), key=lambda x: x[0])[0]
    maxy = max(list(p), key=lambda x: x[1])[1]
    s = [[' '] * (maxx + 1) for i in range(maxy + 1)]
    for x, y in p:
        s[y][x] = '#'
    printmatrix(s)


p, f = parse(inp)

np1 = None
for fx, fy in f:
    np = set()
    for x, y in p:
        if x <= fx or fx == 0:
            nx = x
        else:
            nx = fx - (x - fx)
        if y <= fy or fy == 0:
            ny = y
        else:
            ny = fy - (y - fy)
        np.add((nx, ny))
    p = np
    if np1 is None:
        np1 = len(np)

print(np1)  # 712
printp(p)  # BLHFJPJF
