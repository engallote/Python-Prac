import sys


N, M = map(int, sys.stdin.readline().split())
arr = {}

for i in range(N):
    a, b = sys.stdin.readline().split()
    arr[a] = int(b)

res = 0
for i in range(M):
    a, b = sys.stdin.readline().split()

    if int(b) > arr[a] * 1.05:
        res += 1

print(res)