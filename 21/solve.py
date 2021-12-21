import re
from collections import defaultdict
from itertools import permutations, repeat, combinations, product

inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]

(_, p1) = list(map(int, re.findall(r'-?\d+', inp[0])))
(_, p2) = list(map(int, re.findall(r'-?\d+', inp[1])))
startpos = [p1, p2]


def nextpos(cpos, d):
    cpos += d
    cpos = cpos if cpos <= 10 else (10 if cpos % 10 == 0 else cpos % 10)  # funny!
    return cpos


def part1(pos):
    scores = [0, 0]
    p = 0
    d = 0
    ct = 0
    while scores[0] < 1000 and scores[1] < 1000:
        dt = 0
        for _ in range(3):
            d += 1
            d = d if d <= 100 else d % 100
            dt += d
            ct += 1
        pos[p] = nextpos(pos[p], dt)
        scores[p] += pos[p]
        p = (p + 1) % 2

    return scores[p] * ct


def part2(pos):
    dtimes = defaultdict(int)  # all possible dices (sum of three) and their occurence
    for x, y, z in product([1, 2, 3], repeat=3):
        dtimes[x + y + z] += 1
    maxSteps = 10
    allResults = []
    for p in pos:
        all = dict()
        all[0] = defaultdict(list)
        all[0][p].append((0, 1))
        for stepsNo in range(1, maxSteps + 1):
            starts = all[stepsNo - 1]

            all[stepsNo] = defaultdict(list)
            for (pos, lst) in starts.items():
                for (score, cnt) in lst:
                    if score >= 21:
                        continue
                    for d, times in dtimes.items():

                        npos = nextpos(pos, d)
                        nscore = score + npos
                        ncnt = cnt * times

                        found = False
                        for idx, it in enumerate(all[stepsNo][npos]):
                            if it[0] == nscore:
                                all[stepsNo][npos][idx] = (nscore, ncnt + it[1])
                                found = True
                                break
                        if not found:
                            all[stepsNo][npos].append((nscore, ncnt))
        allResults.append(all)

    p1wins = 0
    p2wins = 0
    for stepsNo in range(1, maxSteps + 1):

        for pos1, lst1 in allResults[0][stepsNo].items():
            for cso1, cnt1 in lst1:

                for pos2, lst2 in allResults[1][stepsNo].items():
                    for cso2, cnt2 in lst2:

                        if cso1 < 21 and cso2 >= 21:
                            p2wins += cnt1 * cnt2

    for stepsNo in range(2, maxSteps + 1):

        for pos1, lst1 in allResults[0][stepsNo].items():
            for cso1, cnt1 in lst1:

                for pos2, lst2 in allResults[1][stepsNo - 1].items():
                    for cso2, cnt2 in lst2:

                        if cso1 >= 21 and cso2 < 21:
                            p1wins += cnt1 * cnt2
    return max(p1wins, p2wins)


print(part1(startpos.copy()))  # 805932
print(part2(startpos.copy()))  # 133029050096658
