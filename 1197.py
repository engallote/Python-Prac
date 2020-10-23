import sys


def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


N, M = map(int, sys.stdin.readline().split())
par = [0 for _ in range(N + 1)]
mp = []

for i in range(1, N + 1):
    par[i] = i

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    mp.append((a, b, c))

mp.sort(key=lambda x: (x[2]))
res = 0

for i in range(M):
    a, b, c = mp[i]

    ap, bp = find(a), find(b)
    if ap == bp:
        continue

    res += c
    par[bp] = ap

print(res)