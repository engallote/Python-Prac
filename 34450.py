import sys


N = int(sys.stdin.readline())
P = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = [0 for _ in range(N)]
for i in arr:
    res[i-P] = 1

for i in range(N):
    if res[i] == 0:
        print(i + P)