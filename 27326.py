import sys


N = int(sys.stdin.readline()) * 2 - 1
arr = list(map(int, sys.stdin.readline().split()))
res = [0 for _ in range(N + 1)]

for i in range(N):
    res[arr[i]] += 1

for i in range(1, N + 1):
    if res[i] == 1:
        print(i)
        break