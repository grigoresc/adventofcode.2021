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

pAdd = lambda p1, p2: [p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2]]
pSub = lambda p1, p2: [p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]]

rx = lambda x, y, z: (x, -z, y)
ry = lambda x, y, z: (-z, y, x)
rz = lambda x, y, z: (-y, x, z)


def allPositions(x, y, z):
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


def rotateScanner(a, rotateIdx):
    ret = []
    for be in a:  # each beacon
        newbe = list(allPositions(*be))[rotateIdx]
        ret.append(newbe)
    return ret


def findCommon(a, b):  # between two scanners a and b
    diffs = []
    for idx in range(POS):
        diffs.append(defaultdict(int))
    for pa in a:
        for pb in b:
            for (idx, pbv) in enumerate(allPositions(pb[0], pb[1], pb[2])):
                (dx, dy, dz) = pSub(pbv, pa)
                diffs[idx][dx] += 1
    for idx in range(POS):
        common = [k for k, v in diffs[idx].items() if v >= 12]
        for diffx in common:
            diffy = None
            diffz = None

            # find common
            common_ab = []
            for pa in a:
                for pb in b:
                    pbv = rotateScanner([pb], idx)[0]

                    (dx, dy, dz) = pSub(pbv, pa)
                    if dx == diffx:
                        if diffy is None:
                            diffy = dy
                        if diffz is None:
                            diffz = dz
                        if diffy == dy and diffz == dz:
                            common_ab.append(pa)
            if len(set(common_ab)) >= 12:
                yield rotateScanner(b, idx), common_ab, (diffx, diffy, diffz)


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
            for (btorotate, commonab, diff) in findCommon(scanner, originalScanners[idxb]):
                scanners[idxb] = btorotate
                offsets[idxb] = pAdd(diff, offsets[idxa])

all = set()
for idx, scanner in scanners.items():
    for be in scanner:  # each beacon
        newbe = tuple(pSub(be, offsets[idx]))
        all.add(newbe)
print(len(all))  # 381

distMax = 0
for idxa, idxb in permutations(range(len(scanners)), 2):
    dist = pSub(offsets[idxa], offsets[idxb])
    dist = abs(dist[0]) + abs(dist[1]) + abs(dist[2])
    distMax = max(dist, distMax)
print(distMax)  # 12201
