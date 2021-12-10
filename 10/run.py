from collections import deque

# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]

m = dict()
m['<'] = '>'
m['['] = ']'
m['{'] = '}'
m['('] = ')'

p = dict()
p[')'] = 3
p[']'] = 57
p['}'] = 1197
p['>'] = 25137

cnt = 0
for l in inp:
    d = deque([])
    for c in l:
        if c in ['<', '[', '{', '(']:
            d.append(c)
        else:
            e = d.pop()
            if m[e] != c:
                cnt += p[c]
                # print("wrong", e, c)
            # else:
        # print("ok")
print("sln1", cnt)  # 240123

p = dict()
p[')'] = 1
p[']'] = 2
p['}'] = 3
p['>'] = 4

counts = []
for l in inp:
    cnt = 0
    d = deque([])
    ok = True
    for c in l:
        if c in ['<', '[', '{', '(']:
            d.append(c)
        else:
            e = d.pop()
            if m[e] != c:
                ok = False
                continue
            # else:
            #     print("ok")
    if not ok:
        continue
    # print(d)
    while len(d) > 0:
        r = d.pop()
        cnt = cnt * 5 + p[m[r]]
    # print(cntl)
    counts.append(cnt)
counts.sort()
print("sln2", counts[int(len(counts) / 2)])  # 3260812321
