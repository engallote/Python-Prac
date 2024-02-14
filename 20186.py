import sys


N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
mx = []
idx = 0
for _ in range(K):
    idx = arr.index(max(arr))
    mx.append((idx, max(arr)))
    arr[idx] = 0

mx.sort(key=lambda x: x[0])

res = 0
for i in range(K):
    res += mx[i][1] - i

print(res)