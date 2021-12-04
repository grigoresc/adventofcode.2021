from typing import Counter
import re

txt = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


inp = [line.strip() for line in txt.split('\n')]
inp = [line.strip() for line in open('input.txt', 'r')]
inp = list(filter(lambda x: x != '', inp))
bingo = inp[0]
bingo
bingo = list(map(int, re.findall(r'\d+', bingo)))


def Init(inp):
    idx = 1
    tickets = []
    while idx < len(inp):
        rows = []
        for l in range(0, 5):
            row = list(map(int, re.findall(r'\d+', inp[idx+l])))
            rows.append(row)
        tickets.append(rows)
        idx += 5
    tickets
    return tickets


def Part1(bingo, tickets):
    round = 1
    found = False
    while not found:
        numbers = set(bingo[0:round])
        numbers
        lastnumber = bingo[round-1]
        found = False
        for idxt in range(0, len(tickets)):
            for i in range(0, 5):
                row = set(tickets[idxt][i])
                if row.issubset(numbers):
                    # print("row", idxt, row)
                    found = True
                    winningticket = idxt
                    break
                col = set(list(zip(*tickets[idxt]))[i])
                if col.issubset(numbers):
                    # print("col", idxt, col)
                    found = True
                    winningticket = idxt
                    break
        round += 1
    return round, lastnumber, winningticket


def Part2(bingo, tickets):
    round = 1
    found = False
    while True:
        numbers = set(bingo[0:round])
        numbers
        lastnumber = bingo[round-1]
        # print("lastn", lastnumber)
        found = False
        tdodel = []
        for idxt in range(0, len(tickets)):
            for i in range(0, 5):
                row = set(tickets[idxt][i])
                if row.issubset(numbers):
                    # print("row", idxt, row)
                    found = True
                    winningticket = idxt
                    tdodel.append(idxt)
                    break
                col = set(list(zip(*tickets[idxt]))[i])
                if col.issubset(numbers):
                    # print("col", idxt, col)
                    found = True
                    winningticket = idxt
                    tdodel.append(idxt)
                    break
        round += 1

        if found and len(tickets) == 1:
            # print("done")
            break

        if found:
            # print("delete")
            tdodel = sorted(tdodel, reverse=True)  # ?
            for idxt in tdodel:
                del tickets[idxt]
    return round, lastnumber, winningticket


def ShowRes(bingo, tickets, round, lastnumber, winningticket):
    # print(winningticket, lastnumber)
    wnumbers = set()
    for i in range(0, 5):
        row = set(tickets[winningticket][i])
        wnumbers = wnumbers.union(row)  # why? (double why..)
    wnumbers
    notw = wnumbers.difference(set(bingo[0:round-1]))
    notw
    print(sum(notw)*lastnumber)


tickets = Init(inp)
round, lastnumber, winningticket = Part1(bingo, tickets)
ShowRes(bingo, tickets, round, lastnumber, winningticket)
# 11774

tickets = Init(inp)
round, lastnumber, winningticket = Part2(bingo, tickets)
ShowRes(bingo, tickets, round, lastnumber, winningticket)
# 4495
