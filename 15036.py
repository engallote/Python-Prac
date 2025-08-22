import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
mim = {0: 2, 1: 1, 2: 1/2, 4:1/4, 8:1/8, 16:1/16}
res = 0

for i in arr:
    res += mim[i]

print(res)