# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]


def pos(x, y):
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
        if 0 <= nx < len(inp) and 0 <= ny < len(inp[0]):
            yield nx, ny


def isLow(x, y):
    for (nx, ny) in pos(x, y):
        if inp[x][y] >= inp[nx][ny]:
            return False
    return True


def findBasin(x, y):
    basin = set()
    toprocess = []
    toprocess.append((x, y))
    while len(toprocess) > 0:
        for (x, y) in toprocess:
            toprocess.remove((x, y))
            basin.add((x, y))
            for (nx, ny) in pos(x, y):
                if inp[nx][ny] < '9' and not (nx, ny) in basin:
                    toprocess.append((nx, ny))

    return basin


# part 1
s = 0
for x in range(0, len(inp)):
    for y in range(0, len(inp[0])):
        if isLow(x, y):
            s += 1 + int(inp[x][y])
print(s)
# 486

# part 2
s = 0
bl = []
for x in range(0, len(inp)):
    for y in range(0, len(inp[0])):
        if isLow(x, y):
            b = findBasin(x, y)
            bl.append(len(b))
            # print(x, y, len(b))
bl.sort(reverse=True)
print(bl[0] * bl[1] * bl[2])
# 1059300
