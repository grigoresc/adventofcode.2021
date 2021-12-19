import math
import re
from collections import defaultdict
from itertools import permutations, combinations, product

inp = [line.strip() for line in open('sample.txt', 'r')]
# inp = [line.strip() for line in open('input.txt', 'r')]
idx = 0
p = []
while idx < len(inp):
    if inp[idx][0] == '-':
        pb = []
        idx += 1
        while idx < len(inp) and inp[idx] != '':
            po = list(map(int, re.findall(r'-?\d+', inp[idx])))
            pb.append((po[0], po[1], po[2]))
            idx += 1
        p.append(pb)
        idx += 1

# def rotate(x, y, z):
#     return [(x, y, z), (z, x, y), (y, z, x)]


rx = lambda x, y, z: (x, -z, y)
ry = lambda x, y, z: (-z, y, x)
rz = lambda x, y, z: (-y, x, z)


# rotc = combinations([0, 1, 2], 3)


# def allrotations(x, y, z):
#     for ix in range(2)


# def move(x, y, z):
#     return [(x, y, z), (-x, y, z), (-x, y, -z), (x, y, -z)] + \
#            [(x, -y, z), (-x, -y, z), (-x, -y, -z), (x, -y, -z)]

# return [(x, y, z), (1000 - x, y, z), (1000 - x, y, 1000 - z), (x, y, 1000 - z)] + \
#        [(x, 1000 - y, z), (1000 - x, 1000 - y, z), (1000 - x, 1000 - y, 1000 - z), (x, 1000 - y, 1000 - z)]


# def pos1(x, y, z):
#     pos = (x, y, z)
#     allpos = set()
#     for tx in range(4):
#         for ty in range(4):
#             for tz in range(4):
#                 cpos = pos
#                 # print("ini", cpos)
#                 for _ in range(tx):
#                     cpos = rx(*cpos)
#                 for _ in range(ty):
#                     cpos = ry(*cpos)
#                 for _ in range(tz):
#                     cpos = rz(*cpos)
#                 # print(cpos)
#                 allpos.add(cpos)
#
#     for x, y, z in allpos:
#         yield x, y, z
#     # return allpos


def pos3(x, y, z):
    pos = (x, y, z)
    allpos = []

    for tx in range(4):
        cpos = pos
        # print("ini", cpos)
        for _ in range(tx):
            cpos = rx(*cpos)

        for _ in range(4):
            cpos = rz(*cpos)
            # print(cpos)
            allpos.append(cpos)

    for ty in [1, 3]:
        cpos = pos
        # print("ini", cpos)
        for _ in range(ty):
            cpos = ry(*cpos)

        for _ in range(4):
            cpos = rz(*cpos)
            # print(cpos)
            allpos.append(cpos)
    for x, y, z in allpos:
        yield x, y, z


def pos(x, y, z):
    return pos3(x, y, z)


#
# def pos2(x, y, z):
#     for rx, ry, rz in rotate(x, y, z):
#         for mx, my, mz in move(rx, ry, rz):
#             yield mx, my, mz
#

# x, y, z = 1, 2, 3
# rot = rotate(x, y, z)
# mov = move(x, y, z)
# print(rotate(x, y, z))
#
# all = list(pos(1, 2, 3))

POS = 24


#
# def rotateset(a):
#     for idx in range(POS):
#         news = set()
#         for ai in a:
#             news.add(list(pos(*ai))[idx])
#         yield news
#         return
#
#
def findCommon(a, b):  # global idx, pb
    diffs = []
    for idx in range(POS):
        diffs.append(defaultdict(int))
    for pa in a:
        for pb in b:
            for (idx, pbv) in enumerate(pos(pb[0], pb[1], pb[2])):
                # print(pbv)
                dx = pbv[0] - pa[0]
                diffs[idx][dx] += 1
                # print(f"pa {pa} {pbv}")
                #     print("common")
    # print("diffs", diffs)
    for idx in range(POS):
        common = [k for k, v in diffs[idx].items() if v >= 12]
        for diffx in common:
            # print(idx, diffx)
            c = 0
            diffy = None
            diffz = None

            # find common
            common_ab = []
            for pa in a:
                for pb in b:
                    pbv = list(pos(pb[0], pb[1], pb[2]))[idx]

                    dx = pbv[0] - pa[0]
                    dy = pbv[1] - pa[1]
                    dz = pbv[2] - pa[2]
                    # print(dx, diffx)
                    if dx == diffx:
                        if diffy == None:
                            diffy = dy
                        if diffz == None:
                            diffz = dz
                        if diffy == dy and diffz == dz:
                            common_ab.append(pa)
                            # print("pos common", pa, pb, pbv)
                            # c += 1
                        # else:
                        #     print("not common!")
            if len(set(common_ab)) >= 12:
                print(f"common ab: {c} {diffx} {diffy} {diffz} {common_ab}")
                yield idx, common_ab, (diffx, diffy, diffz)
    # return None, None


# a = p[0]
# print(a)
# for na in rotateset(a):
#     print(len(na))
#     print(na.pop())
# b = p[1]
# list(findCommon(a, b))
# processed = set()
# while len(rel) < len(p):
results = dict()
for idxa, idxb in permutations(range(len(p)), 2):
    # if idxa not in rel or (idxa, idxb) in processed:
    #     continue
    # if idxb not in rel.keys():
    a = p[idxa]
    b = p[idxb]
    # processed.add((idxa, idxb))
    # for na in rotateset(a):
    print(f"common for {idxa},{idxb}")
    for (rottype, commona, diffs) in findCommon(a, b):
        print(f"found for common for {idxa},{idxb}")
        results[(idxa, idxb)] = (rottype, commona, diffs)
        # print(diffs)
        # rel[idxb] = (rel[idxa][0] + diffs[0], rel[idxa][1] + diffs[1], rel[idxa][2] + diffs[2])

rel = defaultdict()
rel[0] = (0, 0, 0)
# probes = []
while len(rel) < len(p):
    for res in results.items():
        (idxa, idxb) = res[0]
        (rottype, commona, diffs) = res[1]
        print(f"cal {idxa}, {idxb}")

        if idxa not in rel:
            print(f"Skip {idxa}")
            continue
        if idxb in rel:
            print(f"Skip already calculated {idxb}")
            continue
        rel[idxb] = (rel[idxa][0] + diffs[0], \
                     rel[idxa][1] + diffs[1], \
                     rel[idxa][2] + diffs[2])
        # print("Add")
        # for c in commona:
        #     rprob = (c[0] - rel[idxa][0], \
        #              c[1] - rel[idxa][1], \
        #              c[2] - rel[idxa][2])
        #     probes.append(rprob)

all = []
for sc in range(len(p)):
    for be in p[sc]:
        (x, y, z) = (be[0] - rel[sc][0], be[1] - rel[sc][1], be[2] - rel[sc][2])
        all.append((x, y, z))
