import sys


N = int(sys.stdin.readline())
res = 777
for _ in range(3):
    arr = list(map(int, sys.stdin.readline().split()))
    if 7 not in arr:
        res = 0

print(res)