from functools import cache
from itertools import repeat

multiplier = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
ownr = ['A', 'B', 'C', 'D']  # amphipod owner of each room (index based)
hallway = "".join([x for x in repeat(' ', 11)])
MAXCOST = 999999


def tostring(h):
    hc = list(h)
    hc[2] = '_'  # draw with _ not allowed positions
    hc[4] = '_'
    hc[6] = '_'
    hc[8] = '_'
    return "".join([(x if x != ' ' else '.') for x in hc])


def IsFinal(a, b, c, d):
    if ROOMSIZE == 2:
        return a == 'AA' and b == 'BB' and c == 'CC' and d == 'DD'
    if ROOMSIZE == 4:
        return a == 'AAAA' and b == 'BBBB' and c == 'CCCC' and d == 'DDDD'


# compute cost considering the next state
#  - how the rooms are filled - a,b,c,d
#  - how is hallway is filled - h
# le is just for debugging purposes
# returns:
# - cost
# - sln (the steps took so far) - just for debugging purposes
@cache
def Cost(a, b, c, d, h, le):
    if IsFinal(a, b, c, d):
        return 0, "final"

    # print(f"{tostring(h)}")
    all = [a, b, c, d]
    mincost = MAXCOST
    minsln = None
    # find out all possible cases - for each room compute all possible extract ops
    for idx in range(4):
        for extracted, hc, cost in extract(all[idx], idx, h):
            cp = all.copy()
            cp[idx] = extracted
            (subcost, sln) = Cost(cp[0], cp[1], cp[2], cp[3], hc, le + 1)
            totalcost = cost + subcost
            if totalcost < mincost:
                mincost = totalcost
                minsln = f"e{ownr[idx]}:{sln}"

    # find out all possible cases - for each room compute all possible insert ops
    for idx in range(4):
        for inserted, hc, cost in insert(all[idx], idx, h):
            cp = all.copy()
            cp[idx] = inserted
            (subcost, sln) = Cost(cp[0], cp[1], cp[2], cp[3], hc, le + 1)
            totalcost = cost + subcost
            if totalcost < mincost:
                mincost = totalcost
                minsln = f"i{ownr[idx]}:{sln}"

    return mincost, minsln


def extract(room, roomIdx, h):
    ownamp = ownr[roomIdx]
    onlyowner = True
    for amp in room:
        if amp != ownamp:
            onlyowner = False
    if onlyowner:
        return
    steps_up = ROOMSIZE - len(room) + 1
    e = room[-1]
    roomc = room[0:-1]
    for pos in PossiblePositionsForExtract(roomIdx, h):
        hc = h[:pos] + e + h[pos + 1:]  # replace in string
        steps_h = abs(2 * roomIdx + 2 - pos)
        yield roomc, hc, multiplier[e] * (steps_up + steps_h)


def insert(room, roomIdx, h):
    ownamp = ownr[roomIdx]
    onlyowner = True
    for amp in room:
        if amp != ownamp:
            onlyowner = False
    if not onlyowner:
        return
    steps_down = ROOMSIZE - len(room)
    for pos in PossiblePositionsForInsert(roomIdx, h, ownamp):
        hc = h[:pos] + ' ' + h[pos + 1:]  # replace in string
        roomc = room + ownamp
        steps_h = abs(2 * roomIdx + 2 - pos)
        yield roomc, hc, multiplier[ownamp] * (steps_down + steps_h)


def PossiblePositionsForExtract(roomIdx, h):
    epos = 2 + 2 * roomIdx
    cpos = epos + 1
    while cpos < 11 and h[cpos] == ' ':
        yield cpos
        cpos += 2
    if cpos == 11:
        cpos = 10
        if h[cpos] == ' ':
            yield cpos

    cpos = epos - 1
    while cpos >= 0 and h[cpos] == ' ':
        yield cpos
        cpos -= 2
    if cpos == -1:
        cpos = 0
        if h[cpos] == ' ':
            yield cpos


def PossiblePositionsForInsert(roomIdx, h, amp):
    epos = 2 + 2 * roomIdx
    cpos = epos + 1
    while cpos < 11:
        if h[cpos] == ' ':
            cpos += 1
            continue
        if h[cpos] == amp:
            yield cpos
        break
    cpos = epos - 1
    while cpos >= 0:
        if h[cpos] == ' ':
            cpos -= 1
            continue
        if h[cpos] == amp:
            yield cpos
        break


def Sln(a, b, c, d):
    global ROOMSIZE
    ROOMSIZE = len(a)
    cost, sln = Cost(a, b, c, d, hallway, 0)
    return cost


print(Sln('AB', 'DC', 'CB', 'AD'))  # 12521 sample
print(Sln('BC', 'AD', 'BD', 'CA'))  # 12530 input
print(Sln('ADDB', 'DBCC', 'CABB', 'ACAD'))  # 44169 sample 2nd part
print(Sln('BDDC', 'ABCD', 'BABD', 'CCAA'))  # 50492 input 2nd part
