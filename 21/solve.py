import re
from collections import defaultdict
from functools import reduce
from itertools import permutations, repeat

inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]

(_, p1) = list(map(int, re.findall(r'-?\d+', inp[0])))
(_, p2) = list(map(int, re.findall(r'-?\d+', inp[1])))

p = 0
pos = [p1, p2]
sco = [0, 0]
d = 0
ct = 0

while sco[0] < 1000 and sco[1] < 1000:
    dt = 0
    for _ in range(3):
        d += 1
        d = d if d <= 100 else d % 100
        print(f"rolls {d}")
        dt += d
        ct += 1
    pos[p] += dt
    print(f"possible pos {pos[p]}")
    pos[p] = pos[p] if pos[p] <= 10 else (10 if pos[p] % 10 == 0 else pos[p] % 10)  # funny!
    sco[p] += pos[p]
    print(f"{ct} player {p} rolls {dt} moves to {pos[p]} has {sco[p]}")
    p = (p + 1) % 2

print(p, sco[(p) % 2], ct)
print(sco[(p) % 2] * ct)  # 805932
