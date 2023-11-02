import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
num = [0, 0, 0, 0]

for i in arr:
    num[i] += 1

res = 0

flag = True
while flag:
    flag = False
    # 3
    m = min(num[0], num[3])
    if m > 0:
        flag = True
        res += 3 * m
        num[0] -= m
        num[3] -= m

    m = min(num[1], num[2])
    if m > 0:
        flag = True
        res += 3 * m
        num[1] -= m
        num[2] -= m

    # 2
    m = min(num[0], num[2])
    if m > 0:
        flag = True
        res += 2 * m
        num[0] -= m
        num[2] -= m

    m = min(num[1], num[3])
    if m > 0:
        flag = True
        res += 2 * m
        num[1] -= m
        num[3] -= m

    # 1
    m = min(num[0], num[1])
    if m > 0:
        flag = True
        res += m
        num[0] -= m
        num[1] -= m

    m = min(num[1], num[2])
    if m > 0:
        flag = True
        res += m
        num[1] -= m
        num[2] -= m

    m = min(num[2], num[3])
    if m > 0:
        flag = True
        res += m
        num[2] -= m
        num[3] -= m

print(res)