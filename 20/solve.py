import re
from collections import defaultdict
from functools import reduce
from itertools import permutations, repeat

inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]


def parse():
    alg = inp[0]

    img = []
    for i in range(2, len(inp)):
        img.append(inp[i])

    return (alg, img)


def printmatrix(lst):
    # print(lst)
    for line in lst:
        # print("1")
        s = reduce(lambda x, y: x + y, line, "|")  # todo why?
        print(s)


def surround(img, c):
    l = len(img)
    extra = 1
    a = list(repeat(c, l + 2 * extra))
    b = list(repeat(c, extra))
    newimg = []
    for _ in range(extra):
        newimg.append(a.copy())
    for il in img:
        iln = b.copy()
        iln += il
        iln += b.copy()
        newimg.append(iln)
    for _ in range(extra):
        newimg.append(a.copy())
    return newimg


def decode(img):
    newimg = []
    l = len(img)
    decinf = alg[0] if img[0][0] == '.' else alg[512 - 1]
    # print(f"Decode with {decinf}")
    for i in range(0, l):
        newimg.append(list(repeat(' ', l)))
    for i in range(0, l):
        newimg[i][0] = decinf
        newimg[i][l - 1] = decinf
    for j in range(0, l):
        newimg[0][j] = decinf
        newimg[l - 1][j] = decinf

    for i in range(1, l - 1):
        for j in range(1, l - 1):
            v = img[i - 1][j - 1:j + 2] \
                + img[i][j - 1:j + 2] \
                + img[i + 1][j - 1:j + 2]
            s = reduce(lambda x, y: x + y, v, "")
            sb = s.replace('.', '0')
            sb = sb.replace('#', '1')
            newvidx = int(sb, 2)
            newv = alg[newvidx]
            newimg[i][j] = newv

    return newimg


def enhance(img, rounds):
    # printmatrix(img)
    for _ in range(rounds):
        img = surround(img, img[0][0])
        img = decode(img)
        # printmatrix(img)
    cnt = 0
    for i in range(len(img)):
        for j in range(len(img)):
            if img[i][j] == '#':
                cnt += 1
    return cnt


alg, img = parse()

img = surround(img, '.')

sln1 = enhance(img, 2)
print(sln1)  # 5391

sln2 = enhance(img, 50)
print(sln2)  # 16383
