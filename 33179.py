import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = 0

for i in arr:
    res += i // 2
    if i % 2 != 0:
        res += 1

print(res)