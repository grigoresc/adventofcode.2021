l = [int(line.strip()) for line in open("input.txt", 'r')]

cnt = 0
for idx in range(1, len(l)):
    if l[idx] > l[idx-1]:
        cnt += 1
print(cnt)
# 1752

cnt = 0
for idx in range(3, len(l)):
    if l[idx]+l[idx-1]+l[idx-2] > l[idx-1]+l[idx-2]+l[idx-3]:
        cnt += 1
print(cnt)
# 1781
