import sys


N = int(sys.stdin.readline())
mx, cur = 0, 0

for _ in range(N):
    num = int(sys.stdin.readline())
    cur += num

    if cur > 0:
        mx = max(mx, cur)

print(mx + 100)