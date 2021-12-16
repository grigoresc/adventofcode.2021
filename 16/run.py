import math
from collections import Counter, defaultdict

inp = [line.strip() for line in open('input.txt', 'r')][0]

# sample = 'D2FE28'
# sample = '38006F45291200'
# sample = 'EE00D40C823060'
# sample = '8A004A801A8002F478'
# sample = '620080001611562C8802118E34'
# sample = 'C0015000016115A2E0802F182340'  # 23
# sample2 = 'C200B40A82'
# sample2 = '9C0141080250320F1802104A08'
# inp = sample2

b = ''
for h in inp:
    b += '{:04b}'.format(int(h, 16))
lst = []


def parsepackage(idx, packagecnt=None, packagelen=None):
    global b, lst

    firstidx = idx
    cnt = 0

    vals = []

    while True:
        v = b[idx:idx + 3]
        t = b[idx + 3:idx + 6]
        idx += 6
        vv = int(v, 2)
        lst.append(vv)
        tv = int(t, 2)
        if tv == 4:
            cs = ''
            while True:
                c = b[idx + 1:idx + 5]
                last = b[idx] == '0'
                cs += c
                idx += 5
                if last:
                    break
                if idx > len(b):
                    print("Err")
                    break
            n = int(cs, 2)
            vals.append(n)
        else:
            i = b[idx]
            idx += 1
            if i == '0':
                sz = 15
            else:
                sz = 11
            l = b[idx:idx + sz]
            idx += sz

            if i == '0':
                lv0 = int(l, 2)
                (idx, valsi) = parsepackage(idx, None, lv0)

            if i == '1':
                lv1 = int(l, 2)
                (idx, valsi) = parsepackage(idx, lv1, None)

            vo = 0
            if tv == 0:
                vo = sum(valsi)
            elif tv == 1:
                vo = math.prod(valsi)
            elif tv == 2:
                vo = min(valsi)
            elif tv == 3:
                vo = max(valsi)
            elif tv == 5:
                vo = 1 if valsi[0] > valsi[1] else 0
            elif tv == 6:
                vo = 1 if valsi[0] < valsi[1] else 0
            elif tv == 7:
                vo = 1 if valsi[0] == valsi[1] else 0
            vals.append(vo)
        cnt += 1
        if packagecnt is not None:
            if cnt == packagecnt:
                return idx, vals
        elif packagelen is not None:
            if idx - firstidx == packagelen:
                return idx, vals
        else:
            return idx, vals


idx = 0
while idx < len(b):
    (idx, vals) = parsepackage(idx)
    if len(b) - idx < 3 or b[idx:idx + 3] == '000':
        break
print(sum(lst))  # 999
print(vals[0])  # 3408662834145
