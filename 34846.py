import sys


N, M, Q = map(int, sys.stdin.readline().split())
v, n = [0 for _ in range(N)], [0 for _ in range(N)]
d = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    d[a - 1].append(b-1)
    d[b - 1].append(a - 1)

for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        if v[b - 1] == 1:
            continue
        v[b - 1] = 1
        for i in d[b - 1]:
            n[i] += 1
    else:
        print(n[b - 1])