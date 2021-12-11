inp = [line.strip() for line in open('sample.txt', 'r')]

inp = [line.strip() for line in open('input.txt', 'r')]


def pos(x, y):
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1),
                   (x - 1, y - 1)]:
        if 0 <= nx < len(inp) and 0 <= ny < len(inp[0]):
            yield nx, ny


# cp = inp.copy()
e = list()
for x in range(0, len(inp)):
    ei = []
    for y in range(0, len(inp[0])):
        ei.append(int(inp[x][y]))
    e.append(ei)

cnt = 0
rounds = 100
for _ in range(rounds):
    # cp = e.copy()
    for x in range(0, len(inp)):
        for y in range(0, len(inp[0])):
            e[x][y] += 1

    flashes = set()
    while True:
        found = False
        for x in range(0, len(inp)):
            for y in range(0, len(inp[0])):
                if e[x][y] > 9:
                    if not (x, y) in flashes:
                        flashes.add((x, y))
                        found = True
                        for (nx, ny) in pos(x, y):
                            e[nx][ny] += 1
        if not found:
            break
    for (x, y) in flashes:
        e[x][y] = 0
    cnt += len(flashes)
    # break
# 1585
