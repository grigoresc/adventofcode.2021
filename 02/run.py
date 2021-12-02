import re

txt = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

# inp = [line.strip() for line in txt.split('\n')]
inp = [line.strip() for line in open('input.txt', 'r')]


def process(line):
    global h, d
    x = int(re.findall(r'\d+', line)[0])
    if line[0] == 'd':
        d += x
    elif line[0] == 'u':
        d += -x
    elif line[0] == 'f':
        h += x


def process2(line):
    global h, d, aim
    x = int(re.findall(r'\d+', line)[0])
    if line[0] == 'd':
        aim += x
    elif line[0] == 'u':
        aim += -x
    elif line[0] == 'f':
        h += x
        d += aim*x


h = 0
d = 0

for l in inp:
    process(l)

print(d*h)
# 1690020
h = 0
d = 0
aim = 0

for l in inp:
    process2(l)

print(d*h)
# 1408487760
