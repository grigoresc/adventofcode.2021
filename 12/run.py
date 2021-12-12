# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]


def parse(line):
    (s, e) = line.split('-')
    return s, e


lst = list(map(parse, inp))

paths = set(lst)
cnt = 0


def search(start, rpaths: set, smalls: list, dup: int, a: list):
    global cnt
    if start.lower() == start:
        smalls.append(start)
    if start == 'end':
        cnt += 1
        return
    starts = set([x for x in rpaths if x[0] == start or x[1] == start])
    for si in starts:
        next = si[1] if si[0] == start else si[0]
        nextdup = dup
        if next in smalls:
            if nextdup == 0 and next not in ['start', 'end']:
                nextdup = 1
            else:
                continue
        npaths = rpaths.copy()
        na = a.copy()
        if next.lower() == next:
            na.append(next)
        search(next, npaths, smalls.copy(), nextdup, na)


search('start', paths, [], 0, ['start'])
# 3298
print(cnt)  # 93572
