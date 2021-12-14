from collections import Counter
from functools import reduce

inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]


def parse(inp):
    template = ''
    for idx, l in enumerate(inp):
        if len(l) == 0:
            break
        template = l
    r = dict()  # rules
    for l in inp[idx + 1:]:
        (t, fs) = l.split(' -> ')
        r[t] = fs
    return template, r


t, r = parse(inp)

for i in range(10):
    # print(i)
    nt = ''
    for idx, e in enumerate(t):
        if idx > 0:
            f = "" + t[idx - 1] + t[idx]
            nt += r[f]
        nt += e
    t = nt

c = Counter(list(t))
mc = c.most_common()[0]
lc = c.most_common()[-1]
s1 = mc[1] - lc[1]  # 3284
# t1 = t
#
# h = dict()
#
#
# def expand(start, end, times):
#     mid = r[start + end]
#     if (times == 1):
#         return start + mid
#     left = expand(start, mid, times - 1)
#     right = expand(mid, end, times - 1)
#     res = left[1:-1] + right[1:-1]
#     return res
#
#
# t, r = parse(inp)
# for i in range(1):
#     # print(i)
#     nt = ''
#     for idx, e in enumerate(t):
#         if idx > 0:
#             f = expand(t[idx - 1], t[idx], 11)
#             nt += f
#         nt += e
#     t = nt
#
# c = Counter(list(t))
# mc2 = c.most_common()[0]
# lc2 = c.most_common()[-1]
# s2 = mc2[1] - lc2[1]  # 3284
# t2 = t
# print(len(t1), len(t2))
