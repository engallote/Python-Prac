import sys


N = int(sys.stdin.readline())
K = int(sys.stdin.readline()) + 60
res = 0

if N <= K:
    res += N * 1500
else:
    res += K * 1500
    res += (N - K) * 3000

print(res)