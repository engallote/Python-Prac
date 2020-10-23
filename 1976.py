import sys


def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
par = [0 for _ in range(N + 1)]
mp = [[0] for _ in range(N + 1)]

for i in range(1, N + 1):
    par[i] = i

for i in range(1, N + 1):
    mp[i] = list(map(int, sys.stdin.readline().split()))

for i in range(1, N + 1):
    for j in range(N):
        if mp[i][j] == 1:
            ap, bp = find(i), find(j + 1)
            if ap == bp:
                continue
            par[bp] = ap

arr = list(map(int, sys.stdin.readline().split()))
flag = True
for i in range(1, M):
    ap, bp = find(arr[i-1]), find(arr[i])
    if ap != bp:
        flag = False

print("YES" if flag else "NO")