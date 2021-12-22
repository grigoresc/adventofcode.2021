import re
from collections import defaultdict
from functools import reduce
from itertools import permutations, repeat

inp = [line.strip() for line in open('sample2.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]

cubes = []
ons = []
state1 = set()
state0 = set()
for l in inp:
    nl = list(map(int, re.findall(r'-?\d+', l)))

    (x1, x2, y1, y2, z1, z2) = nl
    if abs(x1) > 50 or abs(x2) > 50 or abs(y1) > 50 or abs(y2) > 50 or abs(z1) > 50 or abs(z1) > 50:
        continue

    cubes.append(nl)
    on = True
    if 'off' in l:
        on = False
    ons.append(on)

    (x1, x2, y1, y2, z1, z2) = nl

    for x in range(x1, x2 + 1):
        # if abs(x) > 50:
        # continue
        for y in range(y1, y2 + 1):
            # if abs(y) > 50:
            # continue
            for z in range(z1, z2 + 1):
                # if abs(x) > 50 or abs(y) > 50 or abs(z) > 50:
                # continue
                if on:
                    state1.add((x, y, z))
                else:
                    if (x, y, z) in state1:
                        state1.remove((x, y, z))

print(len(state1))
