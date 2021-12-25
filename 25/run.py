from functools import reduce

# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]

H = len(inp)
W = len(inp[0])

e = set()
s = set()
n = set()

for x in range(H):
    for y in range(W):
        if inp[x][y] == '>':
            e.add((x, y))
        elif inp[x][y] == 'v':
            s.add((x, y))
        else:
            n.add((x, y))

steps = 0
while (True):
    moved = False
    ne = set()  # new East
    for xe, ye in e:
        xc = xe
        yc = ye + 1
        if yc == W:
            yc = 0
        if (xc, yc) not in e and (xc, yc) not in s:
            ne.add((xc, yc))
            moved = True
        else:
            ne.add((xe, ye))
    ns = set()  # new south
    for xs, ys in s:
        xc = xs + 1
        yc = ys
        if xc == H:
            xc = 0
        if (xc, yc) not in ne and (xc, yc) not in s:
            ns.add((xc, yc))
            moved = True
        else:
            ns.add((xs, ys))
    if not moved:
        break
    else:
        steps += 1
        e = ne
        s = ns
print(steps + 1)  # 582
