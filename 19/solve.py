import re
from collections import defaultdict
from itertools import permutations, combinations, product

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


def allOrientations(x, y, z):
    pos = (x, y, z)
    for tx in range(4):
        cpos = pos
        for _ in range(tx):
            cpos = rx(*cpos)
        for _ in range(4):
            cpos = rz(*cpos)
            yield cpos

    for ty in [1, 3]:
        cpos = pos
        for _ in range(ty):
            cpos = ry(*cpos)
        for _ in range(4):
            cpos = rz(*cpos)
            yield cpos


POS = 24


def rotateScanner(a, rotionIdx):
    ret = []
    for be in a:  # each beacon
        newbe = list(allOrientations(*be))[rotionIdx]
        ret.append(newbe)
    return ret


def findCommon(a, b):  # between two scanners a and b
    diffs = []
    for rotationIdx in range(POS):
        diffs.append(defaultdict(int))
    for pa in a:
        for pb in b:
            for (rotationIdx, pbv) in enumerate(allOrientations(pb[0], pb[1], pb[2])):
                (dx, dy, dz) = subCoord(pbv, pa)
                diffs[rotationIdx][dx] += 1
    for rotationIdx in range(POS):
        common = [k for k, v in diffs[rotationIdx].items() if v >= 12]
        for diffx in common:
            diffy = None
            diffz = None

            # find common
            overlap = []
            for pa in a:
                for pb in b:
                    pbv = rotateScanner([pb], rotationIdx)[0]

                    (dx, dy, dz) = subCoord(pbv, pa)
                    if dx == diffx:
                        if diffy is None:
                            diffy = dy
                        if diffz is None:
                            diffz = dz
                        if diffy == dy and diffz == dz:
                            overlap.append(pa)
            if len(set(overlap)) >= 12:
                yield rotateScanner(b, rotationIdx), (diffx, diffy, diffz)


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
