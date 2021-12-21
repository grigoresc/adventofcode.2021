import re
from collections import defaultdict
from functools import reduce
from itertools import permutations, repeat, combinations, product

inp = [line.strip() for line in open('sample.txt', 'r')]
# inp = [line.strip() for line in open('input.txt', 'r')]

(_, p1) = list(map(int, re.findall(r'-?\d+', inp[0])))
(_, p2) = list(map(int, re.findall(r'-?\d+', inp[1])))

pos = [p1, p2]


def part1():
    global allt, p, d, ct, dt, _
    allt = [0, 0]
    p = 0
    d = 0
    ct = 0
    while allt[0] < 1000 and allt[1] < 1000:
        dt = 0
        for _ in range(3):
            d += 1
            d = d if d <= 100 else d % 100
            # print(f"rolls {d}")
            dt += d
            ct += 1
        pos[p] += dt
        # print(f"possible pos {pos[p]}")
        pos[p] = pos[p] if pos[p] <= 10 else (10 if pos[p] % 10 == 0 else pos[p] % 10)  # funny!
        allt[p] += pos[p]
        # print(f"{ct} player {p} rolls {dt} moves to {pos[p]} has {sco[p]}")
        p = (p + 1) % 2
    # print(p, sco[p], ct)
    print(allt[p] * ct)  # 805932


# part1()


def play(pos, pred):
    sco = 0
    cpos = pos
    already21 = False
    for d in pred:
        cpos += d
        cpos = cpos if cpos <= 10 else (10 if cpos % 10 == 0 else cpos % 10)  # funny!
        sco += cpos
        if sco >= 21:
            if already21:
                # print(f"for {pos} and {pred} SKIP")
                return (None, None)
            else:
                already21 = True
    print(f"for {pos} and {pred} have {sco}")
    return (cpos, sco)


maxSteps = 8
dtimes = defaultdict(int)
for x, y, z in product([1, 2, 3], repeat=3):
    dtimes[x + y + z] += 1
    print(x, y, z)

alld = [3, 4, 5, 6, 7, 8, 9]  # all dices posibilities (3 times)
allt = dict()  # all possible transitions from a 'pos' by 'number of steps' to 'another pos'
for start in range(1, 10 + 1):
    allt[start] = dict()
    for stepsNo in range(1, maxSteps + 1):
        allt[start][stepsNo] = dict()  # defaultdict(int)
        seqs = product(alld, repeat=stepsNo)
        for seq in seqs:
            times = 1
            for d in seq:
                times *= dtimes[d]
            (cpos, csco) = play(start, seq)
            if csco == None:
                continue
            if csco not in allt[start][stepsNo].keys():
                allt[start][stepsNo][csco] = 0
            allt[start][stepsNo][csco] += times

p1wins = 0
p2wins = 0
for stepsNo in range(1, maxSteps + 1):
    for csco1, cnt1 in allt[p1][stepsNo].items():
        for csco2, cnt2 in allt[p2][stepsNo].items():
            if csco1 >= 21 and csco2 < 21:
                p1wins += cnt1 * cnt2
            if csco1 < 21 and csco2 >= 21:
                p2wins += cnt1 * cnt2

# expected
# 341960390180808
# 444356092776315

# current - for 7 steps max
# 257767355993576
# 323600927041598
# 271427679324384
# 341948699931462
