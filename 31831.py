import sys

N, M = map(int, sys.stdin.readline().split())
arr, res, day = list(map(int, sys.stdin.readline().split())), 0, 0

for i in arr:
    res += i
    if res < 0:
        res = 0
    elif res >= M:
        day += 1

print(day)