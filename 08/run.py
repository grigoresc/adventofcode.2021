import re
import itertools
from collections import defaultdict
from collections import Counter

inp = [line.strip() for line in open('sample.txt', 'r')]

# inp = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]


inp = [line.strip() for line in open('input.txt', 'r')]


# lst = list(map(int, inp[0].split(',')))


def parse(line):
    (p, d) = line.split(' | ')
    pl = p.split()
    dl = d.split()
    return pl, dl


lst = list(map(parse, inp))
cnt1 = 0
for l in lst:
    f1 = list(filter(lambda x: len(x) == 2, l[1]))
    f4 = list(filter(lambda x: len(x) == 4, l[1]))
    f7 = list(filter(lambda x: len(x) == 3, l[1]))
    f8 = list(filter(lambda x: len(x) == 7, l[1]))
    cnt1 += len(f1) + len(f4) + len(f7) + len(f8)
print(cnt1)  # 288


def sp(s):
    lst = []
    for x in s:
        lst.append(x)
    return lst


def str_to_set(s):
    return set(sp(s))


def decryptl(l):
    global w_b, w_e, w_cf, w_c, w_d, dec
    w1 = set(sp(list(filter(lambda x: len(x) == 2, l[0]))[0]))
    w4 = set(sp(list(filter(lambda x: len(x) == 4, l[0]))[0]))
    w7 = set(sp(list(filter(lambda x: len(x) == 3, l[0]))[0]))
    w8 = set(sp(list(filter(lambda x: len(x) == 7, l[0]))[0]))
    # decode 2 3 5 (least common segms)
    w5_1 = set(sp(list(filter(lambda x: len(x) == 5, l[0]))[0]))
    w5_2 = set(sp(list(filter(lambda x: len(x) == 5, l[0]))[1]))
    w5_3 = set(sp(list(filter(lambda x: len(x) == 5, l[0]))[2]))
    cnt = Counter(list(w5_1) + list(w5_2) + list(w5_3))
    w_be = set(list(map(lambda x: x[0], filter(lambda x: x[1] == 1, cnt.items()))))
    # decode 6 9 0  (least common segms)
    w6_1 = set(sp(list(filter(lambda x: len(x) == 6, l[0]))[0]))
    w6_2 = set(sp(list(filter(lambda x: len(x) == 6, l[0]))[1]))
    w6_3 = set(sp(list(filter(lambda x: len(x) == 6, l[0]))[2]))
    cnt = Counter(list(w6_1) + list(w6_2) + list(w6_3))
    w_cde = set(list(map(lambda x: x[0], filter(lambda x: x[1] == 2, cnt.items()))))
    w5_all = w5_1 | w5_2 | w5_3
    w5_1 - w5_all
    w_a = w7 - w1
    # w9 = w4 + wd
    w_bd = w4 - w1
    w_aeg = w8 - w4
    w_eg = w_aeg - w_a
    w_abdeg = w8 - w1  # ?
    w_bdeg = w8 - w7
    w_b = w_be & w_bd
    w_e = w_be - w_b
    w_d = w_bd - w_b
    w_g = w8 - w1 - w_a - w_b - w_d - w_e
    w_cf = w1
    w_c = w_cde & w_cf
    w_f = w_cf - w_c
    dec = dict()
    dec[list(w_a)[0]] = 'a'
    dec[list(w_b)[0]] = 'b'
    dec[list(w_c)[0]] = 'c'
    dec[list(w_d)[0]] = 'd'
    dec[list(w_e)[0]] = 'e'
    dec[list(w_f)[0]] = 'f'
    dec[list(w_g)[0]] = 'g'
    ret = 0
    for x in l[1]:
        decs = decode(x)
        ret += decs
        # print(x, decs)
        ret = ret * 10
    ret = int(ret / 10)
    return ret


def decode(s):
    global w_b, w_e, w_cf, w_c, w_d, dec
    if len(s) == 2:
        return 1
    if len(s) == 4:
        return 4
    if len(s) == 3:
        return 7
    if len(s) == 7:
        return 8
    if len(s) == 5:
        w = str_to_set(s)
        if len(w_cf - w) == 0:
            return 3
        if len(w_b - w) == 0:
            return 5
        return 2
    if len(s) == 6:
        w = str_to_set(s)
        # print(w_e)
        # print(w)
        if len(w_e - w) == 0 and len(w_d - w) == 0:
            return 6
        if len(w_c - w) == 0 and len(w_d - w) == 0:
            return 9
        return 0


global w_b, w_e, w_cf, w_c, w_d, dec
su = 0
for l in lst:
    d = decryptl(l)
    su += d
    # print(d)
print(sum(map(decryptl, lst)))  # 940724
