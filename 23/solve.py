import re
from collections import defaultdict, deque
from functools import reduce
from itertools import permutations, repeat

# input = ['BACDBCDA']
hallway = [x for x in repeat(' ', 7)]
# input = [['A', 'B'], ['D', 'C'], ['C', 'B'], ['A', 'D']]#sample
input = [['B', 'C'], ['A', 'D'], ['B', 'D'], ['C', 'A']]  # input
rooms = []
for inputr in input:
    room = deque()
    for amp in inputr:
        room.append(amp)
    rooms.append(room)


def hallwaypos2room(hallway, roomidx, roomamp):  # which hallway can move to roomidx
    leftidx = roomidx + 1
    idx = leftidx
    steps = 2
    while idx >= 0:
        if hallway[idx] != ' ':
            if hallway[idx] != roomamp:
                break
            else:
                yield idx, steps
                break
        idx -= 1
        if (idx == 0):
            steps + 1
        else:
            steps += 2
    idx = leftidx + 1
    steps = 2
    while idx < len(hallway):
        if hallway[idx] != ' ':
            if hallway[idx] != roomamp:
                break
            else:
                yield idx, steps
                break
        idx += 1
        if idx == len(hallway) - 1:
            steps += 1
        else:
            steps += 2


def hallwaypos(hallway, roomidx):  # from room, where can I move
    leftidx = roomidx + 1
    idx = leftidx
    steps = 2
    while idx >= 0:
        if hallway[idx] != ' ':
            # print(f"{idx} has {hallway[idx]}")
            break
        # print(idx)
        yield idx, steps
        idx -= 1
        if (idx == 0):
            steps + 1
        else:
            steps += 2
    idx = leftidx + 1
    steps = 2
    while idx < len(hallway):
        if hallway[idx] != ' ':
            # print(f"{idx} has {hallway[idx]}")
            break
        # print(idx)
        yield idx, steps
        idx += 1
        if idx == len(hallway) - 1:
            steps += 1
        else:
            steps += 2


mult = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

costMin = 999999  # 12521 + 1

ownr = ['A', 'B', 'C', 'D']


def move(hallway, level, cost):
    global costMin
    # print(hallway, cost, rooms)
    # print(f"{level}:{cost}/{costMin}")

    if cost >= costMin:
        return

    done = True
    for (idxR, room) in enumerate(rooms):
        if len(room) < 2:
            done = False
            break
        for r in room:
            if r != ownr[idxR]:
                done = False
                break
    if done:
        costMin = min(cost, costMin)
        print("done", costMin, level, hallway, rooms)
        return

    for (idxR, room) in enumerate(rooms):
        if len(room) > 0:
            hasOnlyOwning = True
            for r in room:
                if r != ownr[idxR]:
                    hasOnlyOwning = False

            if not hasOnlyOwning:
                # for this try move out
                amp = room.pop()
                # print(f"[{level}] {amp}")

                for (idxH, steps) in hallwaypos(hallway, idxR):
                    hc = hallway.copy()
                    assert (steps > 0)
                    # crosses one extra room (to the bottom)
                    if len(room) == 0:
                        steps += 1
                    costc = cost + steps * mult[amp]

                    hc[idxH] = amp
                    # print(f"move {amp} to {idx}")
                    move(hc, level + 1, costc)

                room.append(amp)

        if len(room) < 2:
            hasOnlyOwning = True
            for r in room:
                if r != ownr[idxR]:
                    hasOnlyOwning = False
            if hasOnlyOwning:
                amp = ownr[idxR]
                # for this room try populate
                for (idxH, steps) in hallwaypos2room(hallway, idxR, amp):
                    hc = hallway.copy()
                    # print(f"{idxR} {hallway} extract {amp} from {idxH}")
                    hc[idxH] = ' '
                    room.append(amp)
                    # crosses one extra room
                    if len(room) == 1:
                        steps += 1
                    costc = cost + steps * mult[amp]

                    move(hc, level + 1, costc)
                    amp2 = room.pop()
                    assert (amp2 == amp)


move(hallway, 1, 0)
print("done!", costMin)
