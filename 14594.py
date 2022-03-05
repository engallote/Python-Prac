import sys


def find(x):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    arr[i] = i

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    for i in range(a, b):
        ap, bp = find(i), find(i + 1)
        if ap == bp:
            continue
        arr[bp] = ap

res = 0
for i in range(1, N + 1):
    if arr[i] == i:
        res += 1

print(res)