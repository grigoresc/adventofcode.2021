from collections import Counter, defaultdict

# inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')][0]

# sample = 'D2FE28'
# sample = '38006F45291200'
# sample = 'EE00D40C823060'
# sample = '8A004A801A8002F478'
# sample = '620080001611562C8802118E34'
# sample = 'C0015000016115A2E0802F182340'  # 23
# inp = sample
#
b = ''
for h in inp:
    b += '{:04b}'.format(int(h, 16))

# b = '00' + bin(int(inp, 16))[2:]

lst = []


def parsepackage(idx, packagecnt=None, packagelen=None):
    global b
    global lst

    firstidx = idx
    cnt = 0

    print("parsepackage", idx, packagecnt, packagelen)
    while True:
        # while idx < len(b):
        v = b[idx:idx + 3]
        t = b[idx + 3:idx + 6]
        idx += 6
        vv = int(v, 2)
        tv = int(t, 2)
        print("vv", vv)
        print("tv", tv)
        lst.append(vv)
        if tv == 4:
            # print("v", v)
            cs = ''
            print("idx", idx)
            while True:
                c = b[idx + 1:idx + 5]
                last = b[idx] == '0'
                cs += c
                # print(c)
                idx += 5
                if last:
                    break
                if idx > len(b):
                    print("Err")
                    break
                print("idx", idx)
            n = int(cs, 2)

            # lst.append(n)
            print("n", n)
        else:  # if tv in (3, 6):
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
                print("lv0", lv0)
                idx = parsepackage(idx, None, lv0)

            if i == '1':
                lv1 = int(l, 2)
                print("lv1", lv1)
                idx = parsepackage(idx, lv1, None)
        # else:
        #     print("cannot parse, unknown t at idx", t, idx)
        #     return idx
        #     # break
        cnt += 1
        if packagecnt != None:
            if cnt == packagecnt:
                return idx
        elif packagelen != None:
            if idx - firstidx == packagelen:
                return idx
        else:
            return idx


idx = 0
# len(b)
while idx < len(b):
    idx = parsepackage(idx)
    if len(b) - idx < 3 or b[idx:idx + 3] == '000':
        print("break!")
        break
print(sum(lst))
