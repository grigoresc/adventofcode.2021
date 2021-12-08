# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]

lst = list(map(int, inp[0].split(',')))
f = set(lst)


def cost(d):
    return int(d * (d + 1) / 2)


ms = 100000000000000
for p in range(min(f), max(f)):
    s = sum(map(lambda x: abs(p - x), lst))
    ms = min(ms, s)
print(ms)
# 340052

ms = 100000000000000
for p in range(min(f), max(f)):
    s = sum(map(lambda x: cost(abs(p - x)), lst))
    ms = min(ms, s)
print(ms)
# 92948968
