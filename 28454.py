import math
import sys

now = sys.stdin.readline()

N = int(sys.stdin.readline())

res = 0
for _ in range(N):
    date = sys.stdin.readline()

    if now <= date:
        res += 1

print(res)