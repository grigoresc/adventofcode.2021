import re
import itertools


def Read():
    # inp = [line.strip() for line in open('sample.txt', 'r')]
    inp = [line.strip() for line in open('input.txt', 'r')]
    inp = list(filter(lambda x: x != '', inp))
    bingo = inp[0]
    bingo = list(map(int, re.findall(r'\d+', bingo)))

    idx = 1
    tickets = []
    while idx < len(inp):
        rows = []
        for l in range(0, 5):
            row = list(map(int, re.findall(r'\d+', inp[idx+l])))
            rows.append(row)
        tickets.append(rows)
        idx += 5

    return bingo, tickets


def Part1(bingo, tickets):
    round = 0
    while True:
        round += 1
        numbers = set(bingo[0:round])
        lastnumber = bingo[round-1]
        for idxt, ticket in enumerate(tickets):
            for row in ticket:
                if set(row).issubset(numbers):
                    return round, lastnumber, idxt
            for col in zip(*ticket):
                if set(col).issubset(numbers):
                    return round, lastnumber, idxt


def Part2(bingo, tickets):
    round = 0
    found = False
    while True:
        round += 1
        numbers = set(bingo[0:round])
        lastnumber = bingo[round-1]
        found = False
        toDel = set()
        for idxt, ticket in enumerate(tickets):
            for row in ticket:
                if set(row).issubset(numbers):
                    found = True
                    winningticket = idxt
                    toDel.add(idxt)
                    break
            for col in zip(*ticket):
                if set(col).issubset(numbers):
                    found = True
                    winningticket = idxt
                    toDel.add(idxt)
                    break

        if found and len(tickets) == 1:
            break

        if found:
            toDel = sorted(list(toDel), reverse=True)
            for idxt in toDel:
                del tickets[idxt]

    return round, lastnumber, winningticket


def ShowRes(bingo, tickets, round, lastnumber, winningticket):
    all = set(itertools.chain.from_iterable(tickets[winningticket]))
    notwin = all.difference(set(bingo[0:round]))
    print(sum(notwin)*lastnumber)


bingo, tickets = Read()
round, lastnumber, winningticket = Part1(bingo, tickets)
ShowRes(bingo, tickets, round, lastnumber, winningticket)
# 11774

bingo, tickets = Read()
round, lastnumber, winningticket = Part2(bingo, tickets)
ShowRes(bingo, tickets, round, lastnumber, winningticket)
# 4495
