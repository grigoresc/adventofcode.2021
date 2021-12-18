import math

inp = [line.strip() for line in open('sample.txt', 'r')]
inp = [line.strip() for line in open('sample2.txt', 'r')]
inp = [line.strip() for line in open('sample3.txt', 'r')]
inp = [line.strip() for line in open('input.txt', 'r')]

LEFT, RIGHT, VAL = 0, 1, 2
nodes = dict()


def createTree(l, idx, nidx):
    if l[idx] == '[':
        ncnt = len(nodes)
        nodes[ncnt] = {LEFT: None, RIGHT: None, VAL: None}
        nodes[nidx][LEFT] = ncnt
        idx = createTree(l, idx + 1, ncnt)
        assert (l[idx] == ',')
        ncnt = len(nodes)
        nodes[ncnt] = {LEFT: None, RIGHT: None, VAL: None}
        nodes[nidx][RIGHT] = ncnt
        idx = createTree(l, idx + 1, ncnt)
        assert (l[idx] == ']')
        idx += 1
    else:
        sv = ''
        while '0' <= l[idx] <= '9':
            sv += l[idx]
            idx += 1
        nodes[nidx][VAL] = int(sv)
    return idx


def stringTree(nidx):
    v = nodes[nidx][VAL]
    if v is not None:
        return str(v)
    else:
        le = nodes[nidx][LEFT]
        ri = nodes[nidx][RIGHT]

        v = "[" + stringTree(le) + "," + stringTree(ri) + "]"
        return v


def printTree(nidx):
    print(stringTree(nidx))


def add_tree(nidxl, nidxr):
    ncnt = len(nodes)
    nodes[ncnt] = {LEFT: nidxl, RIGHT: nidxr, VAL: None}
    return ncnt


def createTreeFromString(s):
    ncnt = len(nodes)
    nidx = ncnt
    nodes[nidx] = {LEFT: None, RIGHT: None, VAL: None}
    createTree(s, 0, nidx)
    return nidx


def explode_onetime(nidx):
    global nextLeft, nextRight
    global nextLeftV, nextRightV
    global haveExplode
    nextLeft = None
    nextRight = None
    haveExplode = 0
    explode(nidx, 0)
    if haveExplode:
        if nextLeft != None:
            nodes[nextLeft][VAL] += nextLeftV
        if nextRight != None:
            nodes[nextRight][VAL] += nextRightV
    return haveExplode


def explode(nidx, level):
    global nextLeft, nextRight
    global nextLeftV, nextRightV
    global haveExplode

    v = nodes[nidx][VAL]
    if v is not None:
        if not haveExplode:
            nextLeft = nidx
        if haveExplode and nextRight == None:
            nextRight = nidx
        return None
    else:
        le = nodes[nidx][LEFT]
        ri = nodes[nidx][RIGHT]
        if not haveExplode and level > 3 and nodes[le][VAL] != None and nodes[ri][VAL] != None:
            lev = nodes[le][VAL]
            riv = nodes[ri][VAL]
            # print(f"explode {lev} and {riv}")
            nextLeftV = lev
            nextRightV = riv
            nodes[nidx][LEFT] = None
            nodes[nidx][RIGHT] = None
            nodes[nidx][VAL] = 0
            haveExplode = 1
        else:
            explode(le, level + 1)
            explode(ri, level + 1)


def split_onetime(nidx):
    global haveSplit
    haveSplit = False
    split(nidx)
    return haveSplit


def split(nidx):
    global haveSplit

    v = nodes[nidx][VAL]
    if v is not None:
        if not haveSplit and v >= 10:
            haveSplit = True
            (lv, rv) = (math.floor(v / 2), math.ceil(v / 2))
            # print(f"{v} split into {lv} {rv}")
            ncnt = len(nodes)
            nodes[nidx][LEFT] = ncnt
            nodes[ncnt] = {LEFT: None, RIGHT: None, VAL: lv}

            ncnt = len(nodes)
            nodes[nidx][RIGHT] = ncnt
            nodes[ncnt] = {LEFT: None, RIGHT: None, VAL: rv}

            nodes[nidx][VAL] = None
    else:
        le = nodes[nidx][LEFT]
        ri = nodes[nidx][RIGHT]
        split(le)
        split(ri)


def reduce(nidx):
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


sample = "[[[[[9,8],1],2],3],4]"
nidx = createTreeFromString(sample)
explode_onetime(nidx)
assert (stringTree(nidx) == "[[[[0,9],2],3],4]")
printTree(nidx)

sample = "[7,[6,[5,[4,[3,2]]]]]"
nidx = createTreeFromString(sample)
explode_onetime(nidx)
assert (stringTree(nidx) == "[7,[6,[5,[7,0]]]]")
printTree(nidx)

sample = "[[6,[5,[4,[3,2]]]],1]"
nidx = createTreeFromString(sample)
explode_onetime(nidx)
assert (stringTree(nidx) == "[[6,[5,[7,0]]],3]")
printTree(nidx)

sample = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
nidx = createTreeFromString(sample)
explode_onetime(nidx)
assert (stringTree(nidx) == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
printTree(nidx)

sample = "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
nidx = createTreeFromString(sample)
explode_onetime(nidx)
assert (stringTree(nidx) == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
printTree(nidx)

sample = "[[[[0,7],4],[15,[0,13]]],[1,1]]"
nidx = createTreeFromString(sample)
split_onetime(nidx)
split_onetime(nidx)
assert (stringTree(nidx) == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]")
printTree(nidx)

sample = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
nidx = createTreeFromString(sample)
reduce(nidx)
assert (stringTree(nidx) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
printTree(nidx)


def p_mag(nidx):
    v = nodes[nidx][VAL]
    if v is not None:
        return v
    else:
        le = nodes[nidx][LEFT]
        ri = nodes[nidx][RIGHT]

        v = 3 * p_mag(le) + 2 * p_mag(ri)
        return v


root = None
for l in inp:
    t = createTreeFromString(l)
    # printTree(t)
    if root is None:
        root = t
        continue
    root = add_tree(root, t)
    reduce(root)

print(p_mag(root))  # 3486

magMax = 0
for l0 in inp:
    for l1 in inp:
        if l0 != l1:
            c0 = createTreeFromString(l0)
            c1 = createTreeFromString(l1)
            a01 = add_tree(c0, c1)
            reduce(a01)
            mag = p_mag(a01)
            magMax = max(mag, magMax)
print(magMax)  # 4747
