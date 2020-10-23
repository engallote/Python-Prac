import sys


def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


N, M = map(int, sys.stdin.readline().split())
par = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    par[i] = i

while M:
    M -= 1
    v, a, b = map(int, sys.stdin.readline().split())

    if v == 0:
        ap, bp = find(a), find(b)
        par[bp] = ap
    else:
        ap, bp = find(a), find(b)
        if ap == bp:
            print("YES")
        else:
            print("NO")