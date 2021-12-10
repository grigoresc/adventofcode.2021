from collections import deque

# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]

m = {'<': '>', '[': ']', '{': '}', '(': ')'}
p = {')': 3, ']': 57, '}': 1197, '>': 25137}

cnt = 0
for l in inp:
    d = deque([])
    for c in l:
        if c in m.keys():  # opening chars
            d.append(c)
        else:
            e = d.pop()
            if m[e] != c:
                cnt += p[c]
print("sln1", cnt)  # 240123

p = {')': 1, ']': 2, '}': 3, '>': 4}

counts = []
for l in inp:
    cnt = 0
    d = deque([])
    ok = True
    for c in l:
        if c in m.keys():  # opening chars
            d.append(c)
        else:
            e = d.pop()
            if m[e] != c:
                ok = False
                continue
    if not ok:
        continue
    while len(d) > 0:
        r = d.pop()
        cnt = cnt * 5 + p[m[r]]
    counts.append(cnt)
counts.sort()
print("sln2", counts[int(len(counts) / 2)])  # 3260812321
