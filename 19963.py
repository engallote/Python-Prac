import sys


N, M, K = map(int, sys.stdin.readline().split())
first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))
arr = [x for x in range(1, N + 1)]

for i in first:
    if i in arr:
        arr.remove(i)

for i in second:
    if i in arr:
        arr.remove(i)

print(len(arr))
for i in arr:
    print(i, end=' ')