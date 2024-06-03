import sys


N, M = map(int, sys.stdin.readline().split())
arr, res = [], 0

for _ in range(N):
    c = int(sys.stdin.readline())
    arr.append(c)
    res += c

res = M // res
for i in arr:
    print(i * res)