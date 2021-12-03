txt = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

inp = [line.strip() for line in txt.split('\n')]
inp = [line.strip() for line in open('input.txt', 'r')]


def getCnts1(inp):
    cnts1 = [0 for i in range(0, len(inp[0]))]
    for l in inp:
        for i in range(0, len(l)):
            if l[i] == '1':
                cnts1[i] += 1
    return cnts1


def getSln1(lst):
    cnts1 = getCnts1(lst)

    le = len(lst)
    v1 = 0
    v2 = 0
    for i in range(0, len(cnts1)):
        v1 = v1*2
        v2 = v2*2
        if cnts1[i] > le-cnts1[i]:
            v1 += 1
        else:
            v2 += 1
    return v1, v2


v1, v2 = getSln1(inp)
print(v1, v2, v1*v2)
# 841526


def filterCommon(lst, most, least):
    remainings = set(lst)
    idx = 0
    while len(remainings) > 1:
        le = len(remainings)
        cnts1 = getCnts1(list(remainings))

        compare = least
        if cnts1[idx] >= le-cnts1[idx]:
            compare = most
        filtered = [x for x in remainings if x[idx] == compare]
        remainings = filtered
        idx += 1
    return remainings.pop()


ox = filterCommon(inp, '1', '0')
co2 = filterCommon(inp, '0', '1')
oxv = int(ox, 2)
co2v = int(co2, 2)
print(ox, co2, oxv, co2v, oxv*co2v)
# 4790390
