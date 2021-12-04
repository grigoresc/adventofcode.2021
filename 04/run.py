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
    found = False
    while not found:
        round += 1
        numbers = set(bingo[0:round])
        lastnumber = bingo[round-1]
        found = False
        for idxt in range(0, len(tickets)):
            for i in range(0, 5):
                row = set(tickets[idxt][i])
                if row.issubset(numbers):
                    found = True
                    winningticket = idxt
                    break
                col = set(list(zip(*tickets[idxt]))[i])
                if col.issubset(numbers):
                    found = True
                    winningticket = idxt
                    break
    return round, lastnumber, winningticket


def Part2(bingo, tickets):
    round = 0
    found = False
    while True:
        round += 1
        numbers = set(bingo[0:round])
        lastnumber = bingo[round-1]
        found = False
        tdodel = []
        for idxt in range(0, len(tickets)):
            for i in range(0, 5):
                row = set(tickets[idxt][i])
                if row.issubset(numbers):
                    found = True
                    winningticket = idxt
                    tdodel.append(idxt)
                    break
                col = set(list(zip(*tickets[idxt]))[i])
                if col.issubset(numbers):
                    found = True
                    winningticket = idxt
                    tdodel.append(idxt)
                    break

        if found and len(tickets) == 1:
            break

        if found:
            tdodel = reversed(tdodel)
            for idxt in tdodel:
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
