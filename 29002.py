import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
idx, s = 0, sum(arr)

for i in arr:
    if i == s - i:
        idx = i
        continue
    print(i, end=' ')

print(idx)