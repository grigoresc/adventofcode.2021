from collections import Counter, defaultdict

# inp = [line.strip() for line in open('sample.txt', 'r')]
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


def Part1():
    t, r = parse(inp)
    for i in range(10):
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
    s1 = mc[1] - lc[1]
    print(s1)  # 3284


def Part2():
    t, r = parse(inp)
    pairs = defaultdict(int)
    cnts = defaultdict(int)
    for i in t:
        cnts[i] += 1
    for i in range(len(t) - 1):
        pairs[t[i] + t[i + 1]] = 1
    for _ in range(40):
        npairs = defaultdict(int)
        for k, v in pairs.items():
            mid = r[k[0] + k[1]]
            cnts[mid] += v
            left = k[0] + mid
            right = mid + k[1]
            npairs[left] += v
            npairs[right] += v
        pairs = npairs
    c = Counter(cnts)
    mc = c.most_common()[0]
    lc = c.most_common()[-1]
    s2 = mc[1] - lc[1]
    print(s2)  # 4302675529689


Part1()
Part2()
