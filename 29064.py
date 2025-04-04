import sys
import math


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = 0

for i in arr:
    if i == 1:
        res += 1

if res >= N / 2:
    print(0)
else:
    print(math.ceil((N / 2) - res))