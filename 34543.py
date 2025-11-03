import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

res = N * 10

if N >= 3:
    res += 20
if N == 5:
    res += 50
if M > 1000:
    res -= 15

if res < 0:
    res = 0

print(res)