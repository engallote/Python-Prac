import sys


T, X = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
res = 0

for _ in range(N):
    K = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    if X in arr:
        res += 1

if res == N:
    print("YES")
else:
    print("NO")