from functools import cache


@cache
def Calc0(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 1)
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 7
    y *= x
    z += y
    return (x, y, z)


@cache
def Calc1(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 1)
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 8
    y *= x
    z += y
    return (x, y, z)


@cache
def Calc2(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 1)
    x += 13
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 2
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc3(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 1)
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 11
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc4(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 26)
    x += -3
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 6
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc5(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 1)
    x += 10
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 12
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc6(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 1)
    x += 14
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc7(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 26)
    x += -16
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc8(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 1)
    x += 12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 15
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc9(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 26)
    x += -8
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc10(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 26)
    x += -12
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 6
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc11(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 26)
    x += -7
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc12(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 26)
    x += -6
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 8
    y *= x
    z += y

    return (x, y, z)


@cache
def Calc13(w, x, y, z):
    x *= 0
    x += z
    x %= 26
    z = int(z / 26)
    x += -11
    x = 1 if x == w else 0
    x = 1 if x == 0 else 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 5
    y *= x
    z += y
    return (x, y, z)


from itertools import product

# for w in product([1,2,3,4,5,6,7,8,9],14):
# max0
for w in product(reversed([1, 2, 3, 4, 5, 6, 7, 8, 9]), repeat=14):
    # w = list(map(int, '13579246899999'))

    r = (0, 0, 0)
    r = Calc0(w[0], *r)
    r = Calc1(w[1], *r)
    r = Calc2(w[2], *r)
    r = Calc3(w[3], *r)
    r = Calc4(w[4], *r)
    r = Calc5(w[5], *r)
    r = Calc6(w[6], *r)
    r = Calc7(w[7], *r)
    r = Calc8(w[8], *r)
    r = Calc9(w[9], *r)
    r = Calc10(w[10], *r)
    r = Calc11(w[11], *r)
    r = Calc12(w[12], *r)
    r = Calc13(w[13], *r)
    (x, y, z) = r
    print(f"{w} {z}")
    # if z == 0:
    break

lambdas = []
lambdas.append(lambda w, x, y, z: Calc0(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc1(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc2(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc3(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc4(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc5(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc6(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc7(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc8(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc9(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc10(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc11(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc12(w, x, y, z))
lambdas.append(lambda w, x, y, z: Calc13(w, x, y, z))


@cache
def step(k, x, y, z):
    # print(f"step {k} {x} {y} {z}")
    for w in reversed([1, 2, 3, 4, 5, 6, 7, 8, 9]):  # tricky!
        (xn, yn, zn) = lambdas[k](w, x, y, z)
        if k == 13:
            # print(zn)
            if zn == 0:
                print("found")
                return w
            continue
        stepret = step(k + 1, xn, yn, zn)
        if stepret != None:
            newret = f"{w}{stepret}"
            # print(f"newret:{newret}")
            return newret
    return None


res = step(0, 0, 0, 0)
print("done")
# def run(idx):
#     for w0 in product([1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=1):
#         r = (0, 0, 0)
#         res = lambdas[idx](w0[0], *r)
#         # print(f"{w0} {res}")
#         yield w0, res
#
#
# for l in range(14):
#     for r in run(0):
#         print(r)
# 97919997299495
