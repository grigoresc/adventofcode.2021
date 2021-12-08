from collections import Counter

# inp = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]


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


def explode(s):
    return list(s)


def str_to_set(s):
    return set(explode(s))


def decrypt_line(l):
    numbers = l[0]
    # wires for 1 or 4
    w1 = set(explode(list(filter(lambda x: len(x) == 2, numbers))[0]))
    w4 = set(explode(list(filter(lambda x: len(x) == 4, numbers))[0]))

    # decode b,e based on 2 3 5
    w235 = list()  # wires for 2,3,5
    w235 += explode(list(filter(lambda x: len(x) == 5, numbers))[0])
    w235 += explode(list(filter(lambda x: len(x) == 5, numbers))[1])
    w235 += explode(list(filter(lambda x: len(x) == 5, numbers))[2])
    cnt = Counter(w235)
    w_be = set(list(map(lambda x: x[0], filter(lambda x: x[1] == 1, cnt.items()))))  # wires for b,e

    # decode c,d,e based on 6 9 0
    w690 = list()  # wires for 6,9,0
    w690 += explode(list(filter(lambda x: len(x) == 6, numbers))[0])
    w690 += explode(list(filter(lambda x: len(x) == 6, numbers))[1])
    w690 += explode(list(filter(lambda x: len(x) == 6, numbers))[2])
    cnt = Counter(w690)
    w_cde = set(list(map(lambda x: x[0], filter(lambda x: x[1] == 2, cnt.items()))))  # wires for c,d,e

    w_bd = w4 - w1
    w_b = w_be & w_bd
    w_e = w_be - w_b
    w_d = w_bd - w_b
    w_cf = w1
    w_c = w_cde & w_cf
    ret = ""
    for x in l[1]:
        ret += str(decode(x, w_b, w_e, w_cf, w_c, w_d))
    return int(ret, 10)


def decode(s, w_b, w_e, w_cf, w_c, w_d):
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
        if len(w_e - w) == 0 and len(w_d - w) == 0:
            return 6
        if len(w_c - w) == 0 and len(w_d - w) == 0:
            return 9
        return 0


sln2 = sum(map(decrypt_line, lst))
print(sln2)  # 940724
