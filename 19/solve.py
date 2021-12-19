import re
from collections import defaultdict
from itertools import permutations

inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]


def parse():
    idx = 0
    ret = []
    while idx < len(inp):
        if inp[idx][0] == '-':
            sc = []
            idx += 1
            while idx < len(inp) and inp[idx] != '':
                be = list(map(int, re.findall(r'-?\d+', inp[idx])))
                sc.append((be[0], be[1], be[2]))
                idx += 1
            ret.append(sc)
            idx += 1
    return ret


originalScanners = parse()

addCoord = lambda p1, p2: [p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2]]
subCoord = lambda p1, p2: [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]

rx = lambda x, y, z: (x, -z, y)
ry = lambda x, y, z: (-z, y, x)
rz = lambda x, y, z: (-y, x, z)


def allOrientations(pos):
    for tx in range(4):  # rotations around x
        cpos = pos
        for _ in range(tx):
            cpos = rx(*cpos)
        for _ in range(4):  # rotations around z
            cpos = rz(*cpos)
            yield cpos

    for ty in [1, 3]:  # rotations around y
        cpos = pos
        for _ in range(ty):
            cpos = ry(*cpos)
        for _ in range(4):  # rotations around z
            cpos = rz(*cpos)
            yield cpos


def findCommon(a, b):  # between two scanners a and b
    diffs = dict()
    for rotationIdx, rotatedb in enumerate(zip(*map(allOrientations, b))):  # all possible rotations for b
        diffs[rotationIdx] = defaultdict(int)
        for coorda in a:
            for coordb in rotatedb:
                (dx, dy, dz) = subCoord(coordb, coorda)
                diffs[rotationIdx][dx] += 1
        common = [k for k, v in diffs[rotationIdx].items() if v >= 12]
        for diffx in common:
            diffy = None
            diffz = None
            # find common
            overlap = []
            for coorda in a:
                for coordb in rotatedb:
                    (dx, dy, dz) = subCoord(coordb, coorda)
                    if dx == diffx:
                        if diffy is None:
                            diffy = dy
                        if diffz is None:
                            diffz = dz
                        if diffy == dy and diffz == dz:
                            overlap.append(coorda)
            if len(set(overlap)) >= 12:
                yield rotatedb, (diffx, diffy, diffz)


scanners = dict()
scanners[0] = originalScanners[0].copy()
offsets = {0: (0, 0, 0)}
while len(scanners) < len(originalScanners):
    for idxa in range(len(originalScanners)):
        if idxa not in scanners.keys():
            continue
        scanner = scanners[idxa]
        for idxb in range(len(originalScanners)):
            if idxb in scanners.keys():
                continue
            for (rotatedb, diff) in findCommon(scanner, originalScanners[idxb]):
                scanners[idxb] = rotatedb
                offsets[idxb] = addCoord(diff, offsets[idxa])

all = set()
for idx, scanner in scanners.items():
    for be in scanner:  # each beacon
        newbe = tuple(subCoord(be, offsets[idx]))
        all.add(newbe)
print(len(all))  # 381

distMax = 0
for idxa, idxb in permutations(range(len(scanners)), 2):
    dist = subCoord(offsets[idxa], offsets[idxb])
    dist = abs(dist[0]) + abs(dist[1]) + abs(dist[2])
    distMax = max(dist, distMax)
print(distMax)  # 12201
