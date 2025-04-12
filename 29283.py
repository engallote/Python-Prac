import sys


N = int(sys.stdin.readline())

res, s, n = 0, 30, 0
for i in range(1, N + 1):
    if i % 5 == 0:
        n = 1
    res += s
    if n == 1:
        s += 30
        n = 0

print(res)