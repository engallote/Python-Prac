import sys


arr = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    b, l, s = map(float, sys.stdin.readline().split())

    if s >= 17 and l >= 2.0:
        res += arr[int(b)]

print(res)