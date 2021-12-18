import math

inp = [line.strip() for line in open('sample.txt', 'r')]

inp = [line.strip() for line in open('sample2.txt', 'r')]
inp = [line.strip() for line in open('sample3.txt', 'r')]

inp = [line.strip() for line in open('input.txt', 'r')]

LEFT, RIGHT, VAL = 0, 1, 2

node, ncnt = dict(), 0


def processnode(l, idx, nidx):
    global ncnt
    global node
    # left
    # print(f"process {idx} {l[idx]}")
    if l[idx] == '[':
        ncnt += 1
        node[ncnt] = {LEFT: None, RIGHT: None, VAL: None}
        node[nidx][LEFT] = ncnt
        idx = processnode(l, idx + 1, ncnt)
        # print("idx", idx, l[idx])
        assert (l[idx] == ',')
        # idx += 1
        ncnt += 1
        node[ncnt] = {LEFT: None, RIGHT: None, VAL: None}
        node[nidx][RIGHT] = ncnt
        idx = processnode(l, idx + 1, ncnt)
        assert (l[idx] == ']')
        # idx = processnode(l, idx + 1)
        idx += 1
    else:
        sv = ''
        while '0' <= l[idx] <= '9':
            sv += l[idx]
            idx += 1
        node[nidx][VAL] = int(sv)
        # print(sv)
    return idx


def p_string(nidx):
    global node
    s = "["

    v = node[nidx][VAL]
    if v is not None:
        return str(v)
    else:
        le = node[nidx][LEFT]
        ri = node[nidx][RIGHT]

        v = "[" + p_string(le) + "," + p_string(ri) + "]"
        return v


def print_tree(nidx):
    print(p_string(nidx))


def add_tree(nidxl, nidxr):
    global node
    global ncnt

    ncnt += 1
    node[ncnt] = {LEFT: nidxl, RIGHT: nidxr, VAL: None}
    return ncnt


def create(s):
    global ncnt
    global node

    ncnt += 1
    nidx = ncnt
    node[nidx] = {LEFT: None, RIGHT: None, VAL: None}
    processnode(s, 0, nidx)
    return nidx


def explode(nidx):
    while True:
        if not explode_onetime(nidx):
            break
    return nidx


def p_reduce(nidx):
    while True:
        anyop = False
        while True:
            if not explode_onetime(nidx):
                break
            else:
                anyop = True
        if split_onetime(nidx):
            anyop = True
        if not anyop:
            break


def explode_onetime(nidx):
    global node
    global nextleft, nextrigt
    global nextleftv, nextrightv
    global exploded
    nextleft = None
    nextrigt = None
    exploded = 0
    p_explode(nidx, 0)
    # print(f"nexts: {nextleft} / {nextrigt} / {nextleftv} / {nextrightv} / {exploded}")
    # print("f{node[nextleft][VAL]} / {node[nextrigt][VAL]}")
    if exploded:
        if nextleft != None:
            node[nextleft][VAL] += nextleftv
        if nextrigt != None:
            node[nextrigt][VAL] += nextrightv
    return exploded


def p_explode(nidx, level):
    global node
    global nextleft, nextrigt
    global nextleftv, nextrightv
    global exploded

    # print(f"epxloded:{exploded} {level} {nidx}")
    v = node[nidx][VAL]
    if v is not None:
        if not exploded:
            nextleft = nidx
            # print(f"nextleft:{nextleft}")
        if exploded and nextrigt == None:
            nextrigt = nidx
        return None
    else:
        le = node[nidx][LEFT]
        ri = node[nidx][RIGHT]
        if not exploded and level > 3 and node[le][VAL] != None and node[ri][VAL] != None:
            lev = node[le][VAL]
            riv = node[ri][VAL]
            print(f"explode {lev} and {riv}")
            nextleftv = lev
            nextrightv = riv
            node[nidx][LEFT] = None
            node[nidx][RIGHT] = None
            node[nidx][VAL] = 0
            exploded = 1
        else:
            p_explode(le, level + 1)
            p_explode(ri, level + 1)


def p_split(nidx):
    global node
    global splitted
    global ncnt

    # print(f"splitted:{splitted}  {nidx}")
    v = node[nidx][VAL]
    if v is not None:
        # print(f"v={v}")
        if not splitted and v >= 10:
            splitted = True
            (lv, rv) = (math.floor(v / 2), math.ceil(v / 2))
            print(f"{v} split into {lv} {rv}")
            ncnt += 1
            node[nidx][LEFT] = ncnt
            node[ncnt] = {LEFT: None, RIGHT: None, VAL: lv}

            ncnt += 1
            node[nidx][RIGHT] = ncnt
            node[ncnt] = {LEFT: None, RIGHT: None, VAL: rv}

            node[nidx][VAL] = None
            # newnodeidx = create(f"[{lv},{rv}]")
            # creat
            # print(f"nextleft:{nextleft}")
            # nextrigt = nidx
    else:
        le = node[nidx][LEFT]
        ri = node[nidx][RIGHT]
        p_split(le)
        p_split(ri)


def split_onetime(nidx):
    global node
    global splitted
    splitted = False
    p_split(nidx)
    # print(f"nexts: {nextleft} / {nextrigt} / {nextleftv} / {nextrightv} / {exploded}")
    # print("f{node[nextleft][VAL]} / {node[nextrigt][VAL]}")
    return splitted


sample = "[[[[[9,8],1],2],3],4]"
nidx = create(sample)
explode_onetime(nidx)
assert (p_string(nidx) == "[[[[0,9],2],3],4]")
print_tree(nidx)

sample = "[7,[6,[5,[4,[3,2]]]]]"
nidx = create(sample)
explode_onetime(nidx)
assert (p_string(nidx) == "[7,[6,[5,[7,0]]]]")
print_tree(nidx)

sample = "[[6,[5,[4,[3,2]]]],1]"
nidx = create(sample)
explode_onetime(nidx)
assert (p_string(nidx) == "[[6,[5,[7,0]]],3]")
print_tree(nidx)

sample = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
nidx = create(sample)
explode_onetime(nidx)
assert (p_string(nidx) == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
print_tree(nidx)

sample = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
nidx = create(sample)
explode_onetime(nidx)
assert (p_string(nidx) == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
print_tree(nidx)

sample = "[[[[0,7],4],[15,[0,13]]],[1,1]]"
nidx = create(sample)
split_onetime(nidx)
split_onetime(nidx)
assert (p_string(nidx) == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]")
print_tree(nidx)

sample = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
nidx = create(sample)
p_reduce(nidx)
assert (p_string(nidx) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
print_tree(nidx)


def p_mag(nidx):
    global node

    v = node[nidx][VAL]
    if v is not None:
        return v
    else:
        le = node[nidx][LEFT]
        ri = node[nidx][RIGHT]

        v = 3 * p_mag(le) + 2 * p_mag(ri)
        return v


root = None
for l in inp:
    t = create(l)
    print_tree(t)
    if root is None:
        root = t
        continue
    root = add_tree(root, t)
    p_reduce(root)

# print_tree(root)
print(p_mag(root))  # 3486

maxmag = 0
for l0 in inp:
    for l1 in inp:
        if l0 != l1:
            c0 = create(l0)
            c1 = create(l1)
            a01 = add_tree(c0, c1)
            p_reduce(a01)
            mag = p_mag(a01)
            maxmag = max(mag, maxmag)
print(maxmag)  # 4747
