import re
from collections import defaultdict
from functools import reduce
from itertools import permutations, repeat

inp = [line.strip() for line in open('sample3.txt', 'r')]


# inp = [line.strip() for line in open('input.txt', 'r')]


def part1Run(cubes):
    state1 = set()

    for idx, c in enumerate(cubes):
        on = ons[idx]
        # print(c)
        (x1, x2, y1, y2, z1, z2) = c
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
    # return state1


cubesOriginal = []
ons = []
for l in inp:
    nl = list(map(int, re.findall(r'-?\d+', l)))

    (x1, x2, y1, y2, z1, z2) = nl
    # if abs(x1) > 50 or abs(x2) > 50 or abs(y1) > 50 or abs(y2) > 50 or abs(z1) > 50 or abs(z1) > 50:
    #     continue
    # if abs(x1) < 50 or abs(x2) < 50 or abs(y1) < 50 or abs(y2) < 50 or abs(z1) < 50 or abs(z1) < 50:
    #     continue
    cubesOriginal.append(tuple(nl))
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
    elif xs2 <= xs1 <= xe1 <= xe2:
        commonx = (xs2, xe2)
    return commonx


# extract x2 from x1 (actually x1-x2)
def diffPos(xs2, xe2, xs1, xe1):
    # def diffPos(xe1, xe2, xs1, xs2):
    ret = []

    assert (xs1 <= xe1)

    if xs1 < xs2 <= xe1:
        ret.append((xs1, xs2 - 1))
    if xs1 <= xe2 < xe1:
        ret.append((xe2 + 1, xe1))
    return ret


def includes(c1, c2):
    (xs1, xe1, ys1, ye1, zs1, ze1) = c1
    (xs2, xe2, ys2, ye2, zs2, ze2) = c2
    return xs1 <= xs2 <= xe2 <= xe1 \
           and ys1 <= ys2 <= ye2 <= ye1 \
           and zs1 <= zs2 <= ze2 <= ze1


def isintersect(c1, c2):
    cnt = 0
    (xs1, xe1, ys1, ye1, zs1, ze1) = c1
    (xs2, xe2, ys2, ye2, zs2, ze2) = c2
    if xs1 == xs2 and xe1 == xe2:
        cnt += 1
    if ys1 == ys2 and ye1 == ye2:
        cnt += 1
    if zs1 == zs2 and ze1 == ze2:
        cnt += 1
    if cnt >= 2:
        return True
    return False


# def intersect(c1, c2):
#     (xs1, xe1, ys1, ye1, zs1, ze1) = c1
#     (xs2, xe2, ys2, ye2, zs2, ze2) = c2
#     commonx = commonPos(xe1, xe2, xs1, xs2)
#     commony = commonPos(ye1, ye2, ys1, ys2)
#     commonz = commonPos(ze1, ze2, zs1, zs2)
#     if commonx != None and commony != None and commonz != None:
#         return (commonx[0], commonx[1], commony[0], commony[1], commonz[0], commonz[1])
#     return None


def CubeDebug(cubes: list):
    if cubes == None:
        return "NONE"
    s = f"[cnt={len(cubes)}";
    for c in cubes:
        s += f" sz={CubeSize([c])} {c[0]},{c[1]},{c[2]},{c[3]},{c[4]},{c[5]}"
    s += "]"
    return s


def CubeSize(cubes):
    total = 0
    for c in cubes:
        sz = abs(c[1] - c[0] + 1) * abs(c[3] - c[2] + 1) * abs(c[5] - c[4] + 1)
        total += sz
    return total


def runPart2(cubes):
    acubes = set()
    for idx, c in enumerate(cubes):
        # print("-------------------------------------------")
        print(f"process cube {idx}: {CubeDebug([c])} {c}")
        touchedcubes = set()
        cubesonlef = set()
        for existingc in acubes:
            diffcubes = diff(existingc, c)

            if diffcubes != None:
                touchedcubes.add(existingc)
                # print("Add", diffcubes)
                cubesonlef = cubesonlef | diffcubes

        # sets causign problems..
        if ons[idx]:
            for ct in touchedcubes:
                # print(f"touched cube {CubeDebug([ct])}")
                acubes.remove(ct)
            for cl in cubesonlef:
                # print(f"left cube {CubeDebug([cl])}")
                acubes.add(cl)
            # print(f"on:add {CubeDebug(cubesonlef)} remove {CubeDebug(touchedcubes)}")
            acubes.add(c)
        else:
            for ct in touchedcubes:
                # print(f"touched cube {CubeDebug([ct])}")
                acubes.remove(ct)
            for cl in cubesonlef:
                # print(f"left cube {CubeDebug([cl])}")
                acubes.add(cl)
            # acubes = acubes.difference(touchedcubes)
            # acubes = acubes | cubesonlef
            # for ct in touchedcubes:
            #     acubes = acubes.difference(ct)
            # for cl in cubesonlef:
            #     acubes.add(cl)
            # if c in acubes:
            # acubes.remove(c)
            # acubes.add(c)
            # print(f"off:add {CubeDebug(cubesonlef)} remove {CubeDebug(touchedcubes)}")
        # print(f"status {CubeDebug(acubes)}")
        yield len(acubes)


def CubeExplodeGeneric(x1, x2, xs2, xe2):
    # print(f"{x1} {x2} {xs2} {xe2}")
    if x1 == xs2 or x2 == xe2:
        yield x1, x2
        return

    if xs2 <= x1 <= xe2 <= x2:
        yield x1, xe2
        yield xe2 + 1, x2
    elif x1 <= xs2 <= xe2 <= x2:
        yield x1, xs2 - 1
        yield xe2 + 1, x2
        yield xs2, xe2
    elif x1 <= xs2 <= x2:
        yield x1, xs2 - 1
        yield xs2, x2
    else:
        yield x1, x2


def CubeExplodeX(cube: tuple, xs2, xe2):
    # print(f"explode x {cube} {CubeDebug([cube])}")
    (x1, x2, y1, y2, z1, z2) = cube
    ret = set()
    for nx1, nx2 in CubeExplodeGeneric(x1, x2, xs2, xe2):
        assert (nx1 <= nx2)
        ncube = (nx1, nx2, y1, y2, z1, z2)
        ret.add(ncube)
    # print(f"new cubes {CubeDebug(list(ret))}")
    return ret


def CubeExplodeY(cube: tuple, ys2, ye2):
    # print(f"explode y {cube} {CubeDebug([cube])}")
    (x1, x2, y1, y2, z1, z2) = cube
    ret = set()
    for ny1, ny2 in CubeExplodeGeneric(y1, y2, ys2, ye2):
        # print(f"{y1},{y2},{ys2},{ye2} -> {ny1},{ny2}")
        assert (ny1 <= ny2)
        ncube = (x1, x2, ny1, ny2, z1, z2)
        ret.add(ncube)
    # print(f"new cubes {CubeDebug(list(ret))}")
    return ret


def CubeExplodeZ(cube: tuple, zs2, ze2):
    # print(f"explode z {cube} {CubeDebug([cube])}")
    (x1, x2, y1, y2, z1, z2) = cube
    ret = set()
    for nz1, nz2 in CubeExplodeGeneric(z1, z2, zs2, ze2):
        assert (nz1 <= nz2)
        ncube = (x1, x2, y1, y2, nz1, nz2)
        ret.add(ncube)
    # print(f"new cubes {CubeDebug(list(ret))}")
    return ret


# tests
cube = (-5, 47, 1, 2, 3, 4)
ec = CubeExplodeX(cube, -44, 5)
ecexpected = set([(-5, 5, 1, 2, 3, 4), (6, 47, 1, 2, 3, 4)])
print(ec)
assert (ecexpected == ec)

cube = (1, 2, 3, 4, -19, 33)
ec = CubeExplodeZ(cube, -14, 35)
ecexpected = set([(1, 2, 3, 4, -19, -15), (1, 2, 3, 4, -14, 33)])
print(ec)
assert (ecexpected == ec)

cube = (1, 2, 3, 4, 9, 11)
ec = CubeExplodeZ(cube, 9, 11)
ecexpected = set([(1, 2, 3, 4, 9, 11)])
print(ec)
assert (ecexpected == ec)

cube = (1, 2, 3, 4, 9, 11)
ec = CubeExplodeZ(cube, 9, 10)
ecexpected = set([(1, 2, 3, 4, 9, 11)])
print(ec)


# assert (ecexpected == ec)


def CubeSum(cubes: list):
    t = 0
    for cube in cubes:
        t += CubeSize([cube])
    return t


def CubeExplode(cube1: tuple, cube2: tuple):
    # print(f"explode {cube1} by {cube2}")
    origsum = CubeSum([cube1])
    byX = CubeExplodeX(cube1, cube2[0], cube2[1])
    byY = set()
    for cube in byX:
        byY |= CubeExplodeY(cube, cube2[2], cube2[3])
    byZ = set()
    for cube in byY:
        byZ |= CubeExplodeZ(cube, cube2[4], cube2[5])
    ret = byZ
    newsum = CubeSum(list(ret))
    # print(f"orig vs new sum {origsum}, {newsum}")
    # print(f"resulted explode is {ret}")
    assert (newsum == origsum)
    return ret


def diff(c1, c2):
    (xs1, xe1, ys1, ye1, zs1, ze1) = c1
    (xs2, xe2, ys2, ye2, zs2, ze2) = c2

    splitc1 = CubeExplode(c1, c2)
    # print(f"splt is {splitc1}")
    newc = set()
    for cube in splitc1:
        # print(f"compare {cube} vs {c2}")
        inte = includes(c2, cube)
        # print(f"int is {inte}")
        if not inte:
            newc.add(cube)
        # else:
        #     print("comon, will remove")
    # print(f"diff is {newc}")
    return newc
    # diffx = diffPos(xs2, xe2, xs1, xe1)
    # diffy = diffPos(ys2, ye2, ys1, ye1)
    # diffz = diffPos(zs2, ze2, zs1, ze1)
    # if len(diffx) == 0 or len(diffy) == 0 or len(diffz) == 0:
    #     # print("return c1")
    #     return None
    # ret = set()
    # for dx in diffx:
    #     for dy in diffy:
    #         for dz in diffz:
    #             ret.add((dx[0], dx[1], dy[0], dy[1], dz[0], dz[1]))
    # print(ret)
    # return ret


# dc = diff(cubesOriginal[0], cubesOriginal[1])
# CubeDebug(dc)

# cubes = CubeExplode(cubesOriginal[0], cubesOriginal[1])
# cnt = 0
# for cubes1, cubes2 in zip(part1Run(cubesOriginal.copy()), runPart2(cubesOriginal.copy())):
#     print(f"current cubes1:{cubes1}")
#     print(f"current cubes2:{cubes2}")
#     print(f"iteration {cnt} {ons[cnt]}")
#     print("p1", len(cubes1))
#     print("p2", CubeSize(cubes2))
#     # cnt += 1
#     # if cnt == 6:
#     #     break
# for cubes1 in part1Run(cubesOriginal.copy()):
for cubes2 in runPart2(cubesOriginal.copy()):
    # print(f"current cubes1:{cubes1}")
    # print(f"current cubes2:{cubes2}")
    # print(f"iteration {cnt} {ons[cnt]}")
    # print("p1", len(cubes1))
    # print("p2", CubeSize(cubes2))
    #     # cnt += 1
    #     # if cnt == 6:
    #     #     break
    print(cubes2)
# cubes1 = part1Run(cubesOriginal.copy())
# print(len(cubes1))
# print(total)
# 18504237586281391 - mine
# 2758514936282235 - real (sample3)
# 882613 - mine
# 474140 - real (sample3)

# 25872 common after 1st iteration
# total after 248314
# CubeDebug([cubesOriginal[0]])
# CubeDebug([cubesOriginal[1]])
#
#
# dc = diff(cubesOriginal[1], cubesOriginal[0])
# CubeDebug(dc)
#
# ic = intersect(cubesOriginal[1], cubesOriginal[0])
# CubeDebug([ic])
