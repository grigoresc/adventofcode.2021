import re
from collections import defaultdict
from functools import reduce
from itertools import permutations, repeat

inp = [line.strip() for line in open('sample3.txt', 'r')]


# inp = [line.strip() for line in open('input.txt', 'r')]


def part1Run():
    cubes = []
    ons = []
    state1 = set()
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
        yield state1


cubes = []
ons = []
for l in inp:
    nl = list(map(int, re.findall(r'-?\d+', l)))
    (x1, x2, y1, y2, z1, z2) = nl

    (x1, x2, y1, y2, z1, z2) = nl
    if abs(x1) > 50 or abs(x2) > 50 or abs(y1) > 50 or abs(y2) > 50 or abs(z1) > 50 or abs(z1) > 50:
        continue
    cubes.append(tuple(nl))
    on = True
    if 'off' in l:
        on = False
    ons.append(on)


def commonPos(xe1, xe2, xs1, xs2):
    commonx = None
    if xs1 <= xs2 <= xe1:
        commonx = (xs2, xe1)
    elif xs1 <= xe2 <= xe1:
        commonx = (xs1, xe2)
    return commonx


def diffPos(xe1, xe2, xs1, xs2):
    ret = []
    assert (xs1 < xe1)
    if xs1 < xs2 <= xe1:
        ret.append((xs1, xs2 - 1))
    if xs1 <= xe2 < xe1:
        ret.append((xe2 + 1, xe1))
    return ret


def intersect(c1, c2):
    (xs1, xe1, ys1, ye1, zs1, ze1) = c1
    (xs2, xe2, ys2, ye2, zs2, ze2) = c2
    commonx = commonPos(xe1, xe2, xs1, xs2)
    commony = commonPos(ye1, ye2, ys1, ys2)
    commonz = commonPos(ze1, ze2, zs1, zs2)
    if commonx != None and commony != None and commonz != None:
        return (commonx[0], commonx[1], commony[0], commony[1], commonz[0], commonz)
    return None


def diff(c1, c2):
    (xs1, xe1, ys1, ye1, zs1, ze1) = c1
    (xs2, xe2, ys2, ye2, zs2, ze2) = c2
    diffx = diffPos(xe1, xe2, xs1, xs2)
    diffy = diffPos(ye1, ye2, ys1, ys2)
    diffz = diffPos(ze1, ze2, zs1, zs2)
    if len(diffx) == 0 or len(diffy) == 0 or len(diffz) == 0:
        # print("return c1")
        return None
    for dx in diffx:
        for dy in diffy:
            for dz in diffz:
                return (dx[0], dx[1], dy[0], dy[1], dz[0], dz[1])


def CubeSize(cubes):
    total = 0
    for c in cubes:
        sz = abs(c[1] - c[0]) * abs(c[3] - c[2]) * abs(c[5] - c[4])
        total += sz
    return total


def runPart2():
    acubes = set()
    for idx, c in enumerate(cubes):
        print(f"process cube {idx} size {CubeSize([c])}")
        touchedcubes = set()
        cubesonlef = set()
        for existingc in acubes:
            diffcubes = diff(existingc, c)
            if diffcubes != None:
                touchedcubes.add(existingc)
                cubesonlef.add(diffcubes)

        if ons[idx]:
            for ct in touchedcubes:
                acubes = acubes.difference(ct)
            for cl in cubesonlef:
                acubes.add(cl)
            print(f"on:add {len(cubesonlef)} remove {len(touchedcubes)}")
            acubes.add(c)
        else:
            acubes = acubes.difference(touchedcubes)
            acubes = acubes | cubesonlef
            # for ct in touchedcubes:
            #     acubes = acubes.difference(ct)
            # for cl in cubesonlef:
            #     acubes.add(cl)
            print(f"off:add {len(cubesonlef)} remove {len(touchedcubes)}")
        yield acubes


for cubes1 in part1Run():
    print(len(cubes1))

for cubes2 in runPart2():
    print(CubeSize(cubes2))

# print(total)
# 18504237586281391 - mine
# 2758514936282235 - real (sample3)
# 817294 - mine
# 474140 - real (sample3)
